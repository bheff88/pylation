import numpy as np
import pandas as pd
import time
from multiprocessing import Pool
from functools import partial

data = 0
pathway = '/home/braden/Current_Project/Data/'


def f(N_stations, i):
    x = data[i][~np.isnan(data[i]).any(axis=1)]
    np.random.shuffle(x)
    return x[:N_stations]


class Year:

    def __init__(self, year, N_dt, N_stations):
        self.year = year
        self.N_dt = N_dt
        self.N_stations = N_stations
        self.new_p = 0

    def reshape_full_set(self):
        N_dt = self.N_dt
        df = pd.read_hdf(pathway + str(self.year) + '.hdf')
        v = df.values
        filename = 'DB/Data/Station_Information.hdf'
        s = pd.read_hdf(filename).T
        for val in s.columns.values:
            if val in df.columns.values:
                continue
            else:
                s = s.drop([val], axis=1)
        for val in df.columns.values:
            if val in s.columns.values:
                continue
            else:
                df = df.drop([val], axis=1)
        p = np.asarray([np.asarray([x for x in df.iloc[i:i+N_dt].values])
                        for i in range(len(v[:])-N_dt)])
        p = p.swapaxes(1, 2)
        hr = np.array(df.index.hour[self.N_dt:])
        mn = np.array(df.index.minute[self.N_dt:])
        tod = hr + mn/60
        cos_tod = np.cos(np.pi*tod*2/24)
        sin_tod = np.sin(np.pi*tod*2/24)
        cos_tod = cos_tod.reshape(cos_tod.shape[0], 1, 1)
        sin_tod = sin_tod.reshape(sin_tod.shape[0], 1, 1)
        cos_tod = np.repeat(cos_tod, p.shape[1], 1)
        sin_tod = np.repeat(sin_tod, p.shape[1], 1)
        new_s = s.T.drop(['Geom_Lat', 'Geom_Long', 'Midnight',
                          'Conj_Lat', 'Conj_Long', 'Elevation',
                          'Declination', 'dH', 'dm'], axis=1).T
        new_s = new_s.values.astype('float')
        new_s = new_s.swapaxes(0, 1)
        new_s = new_s.reshape(1, new_s.shape[0], new_s.shape[1])
        new_s = np.repeat(new_s, p.shape[0], axis=0)
        new_p = np.append(p, new_s, axis=-1)
        new_p = np.append(new_p, cos_tod, axis=-1)
        new_p = np.append(new_p, sin_tod, axis=-1)

        self.new_p = new_p
        global data
        data = new_p
        return

    def parallelize(self):
        self.reshape_full_set()
        shp = self.new_p.shape[0]
        pool = Pool(processes=6)
        func = partial(f, self.N_stations)
        B = pool.map(func, range(shp))
        pool.close()
        pool.join()
        return B


def main(strt_yr=2007, end_yr=2017, N_dt=12, N_stations=15, fname='Train.npz'):

    t = time.time()
    collection = Year(strt_yr, N_dt, N_stations).parallelize()
    collection = np.asarray(collection)

    for year in range(strt_yr, end_yr):
        print('----')
        print('Beginning:', year)
        df = Year(year, N_dt, N_stations).parallelize()
        df = np.asarray(df)
        collection = np.append(collection, df, axis=0)

    np.savez(fname, collection)

    print('')
    print('')
    print('')
    print('Processing is now complete and took about:',
          (time.time() - t)//60, 'minutes')
    print('Saved to:', fname, 'in your your current directory.')
    return collection.shape


def mod_data_structure():
    x1 = np.load('Train_1.npz')['arr_0']
    x2 = np.load('Train_2.npz')['arr_0']
    x3 = np.load('Train_2.npz')['arr_0']
    Y = x1[:, 0, :]
    coords = Y[:, -5:-3]
    index2 = [[i for i in range(15) if x2[j, i, -5:-3] not in coords[j]] for j in range(len(coords))]
    index3 = [[i for i in range(15) if x3[j, i, -5:-3] not in coords[j]] for j in range(len(coords))]
    drops2 = np.asarray([idx if len(idx) <= 14 else idx[1:] for idx in index2])
    drops3 = np.asarray([idx if len(idx) <= 14 else idx[1:] for idx in index3])
    X3 = np.asarray([x3[i, drop] for i, drop in enumerate(drops3) if len(drop) == 14 and len(drops2[i]) == 14])
    X2 = np.asarray([x2[i, drop] for i, drop in enumerate(drops2) if len(drop) == 14 and len(drops3[i]) == 14])
    X1 = np.asarray([x1[i] for i, drop in enumerate(drops2) if len(drop) == 14 and len(drops3[i])==14])
    return X3, X2, X1


def save_modified_data():
    X3, X2, X1 = mod_data_structure()
    np.savez('Train_2_ready.npz', X2)
    np.savez('Train_3_ready.npz', X3)
    np.savez('Train_1_ready.npz', X1)
    print('All data saved, processing complete')
    return


if __name__ == '__main__':
    for i in range(1, 4):
        shape = main(end_year=2017,
                     N_dt=12,
                     N_stations=15,
                     fname='Train_' + str(i) + '.npz')
    save_modified_data()

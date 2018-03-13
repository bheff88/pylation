import numpy as np
import pandas as pd
import spacepy.datamodel as dm
from spacepy import pycdf
import os
import pickleshare as ps
from multiprocessing import Process


db_pathway = '~/Database'
db = ps.PickleShareDB(db_pathway)


def data_in(f_name, LOCATION):
    try:
        data = dm.fromCDF(f_name).copy()
    except:
        try:
            data = pycdf.CDF(f_name)
        except:
            print('Issue with:', f_name)
            return pd.DataFrame(), False

    time = data['thg_mag_' + LOCATION + '_time'].copy()
    D = data['thg_mag_' + LOCATION].copy()
    df = pd.DataFrame(D, index=time)
    df.index = pd.to_datetime(df.index, unit='s')
    df = df.resample('1min').mean()

    return df, True

def get_data(LOCATION, YEAR):
    pathway = '/Data/Magnetometers/' + LOCATION + '/' + str(YEAR) + '/'
    fname = 'Corrupt/' + LOCATION + '/' + str(YEAR) + '/bad_files'
    db[fname] = []
    try:
        file_list = sorted(os.listdir(pathway))
        year_present = True
    except:
        year_present = False
        print(str(YEAR) + '---' + LOCATION, 'not in database')
    if year_present and (len(file_list) > 1):
        df_full, G = data_in(pathway + file_list[0], LOCATION)
        for file in file_list[1:]:
            df, G = data_in(pathway + file, LOCATION)
            if G:
                df_full = pd.concat((df_full, df), axis=0)
        fname = '/Data/HDF/' + str(YEAR) + '/' + LOCATION + '.hdf'
        print(fname, YEAR, 'Complete')
        df_full = df_full.drop_duplicates()
        df_dbdt = df_full.diff()**2
        df_dbdt = np.log(df_dbdt.sum(axis=1)**(1/2))
        df_dbdt = df_dbdt.replace(np.inf, np.nan).replace(-np.inf, np.nan).dropna()
        df_dbdt = df_dbdt[str(YEAR)].resample('5min', label='left').mean()
        df_dbdt.to_hdf(fname, key='Y' + str(YEAR), mode='w', format='f')
    else:
        print('Exiting....')
    return


def step1(LOCATION):
    procs = []
    for YEAR in range(2007, 2018):
        proc = Process(target=get_data, name=LOCATION + str(YEAR),
                       args=(LOCATION, YEAR))
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()
    return


def main():
    pathway = '/Data/Magnetometers/'
    stations = sorted(os.listdir(pathway))[70:]
    procs = []
    for j in range(len(stations)):
        LOCATION = stations[j]
        if LOCATION != 'han':
            proc = Process(target=step1, name=LOCATION,
                           args=(LOCATION,))
            procs.append(proc)
            proc.start()
        if (j + 1) % 15 == 0:
            print(procs)
            for proc in procs:
                proc.join()
                print(proc)
            procs=[]

    for proc in procs:
        proc.join()

    return



def merge_data(YEAR):

    pathway = '/Data/HDF/' + str(YEAR) + '/'
    try:
        file_list = sorted(os.listdir(pathway))
        year_present = True
    except:
        year_present = False
        print(str(YEAR) + '--- not in database')


    start = str(YEAR) + '-01-01-00:00:00'
    end = str(YEAR) + '-12-31-23:55:00'
    tindex = pd.date_range(start=start, end=end, freq='5min')
    df = pd.DataFrame(index=tindex)
    if year_present and (len(file_list) > 1):
        name = file_list[0].split('.')[0]
        df[name] = pd.read_hdf(pathway + file_list[0])
        for file in file_list:
            name = file.split('.')[0]
            df[name] = pd.read_hdf(pathway + file)

        fname = '/Data/HDF_Full/' + str(YEAR) + '.hdf'
        df.to_hdf(fname, key='Y' + str(YEAR), mode='w', format='f')
        print(YEAR, df.shape)
    else:
        print('Exiting....')
    return
#p = np.asarray([np.asarray([x for x in v[i:i+10]]) for i in range(len(v[:30])-1)])
#p = np.asarray([np.asarray([x for x in df.iloc[i:i+10].values]) for i in range(len(v[:50])-10)])
#p = p.swapaxes(1,2)

#main()

def find_missing():
    stations = sorted(os.listdir('/Data/Magnetometers/'))
    procs = []
    for YEAR in range(2007,2018):
        for station in stations:
            try:
                file_list = sorted(os.listdir('/Data/Magnetometers/' + station + '/' + str(YEAR)))
                if len(file_list) > 1:
                    year_present = True
                else:
                    year_present = False
            except:
                year_present = False
            if year_present:
                n_file_list = sorted(os.listdir('/Data/HDF/' + str(YEAR)))

                if station + '.hdf' not in n_file_list:
                    print(station, YEAR)
                    proc = Process(target=get_data, name=station + str(YEAR),
                                   args=(station, YEAR))
                    procs.append(proc)
                    proc.start()
                    if len(procs) == 15:
                        print(procs)
                        for proc in procs:
                            proc.join()
                            print(proc)
                        procs=[]

    if len(procs) > 2:
        for proc in procs:
            proc.join()
    return

#find_missing()
#    merge_data(YEAR)

#fname = '/Data/HDF_Full/'
#files = sorted(os.listdir(fname))
#
#for file in files:
#    df = pd.read_hdf(fname + file)
#    print(df.shape)





















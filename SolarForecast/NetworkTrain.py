import numpy as np
from Development import get_model_2
from Relational import Modulated_Relational
from keras.layers.advanced_activations import LeakyReLU
import pickleshare as ps
pathway = '~/Current_Project/Main/DB'
db = ps.PickleShareDB(pathway)


def normalization():
    x1 = np.load('DB/TrainData/Train_1_ready.npz')['arr_0']
    x2 = np.load('DB/TrainData/Train_2_ready.npz')['arr_0']
    x3 = np.load('DB/TrainData/Train_3_ready.npz')['arr_0']

    def normalize(x):
        x[:, :, :-5] = x[:, :, :-5]/20
        x[:, :, -5] = x[:, :, -5]/90
        x[:, :, -4] = x[:, :, -4]/360
        x[:, :, -3] = x[:, :, -3]/24
        return x

    x1 = normalize(x1)
    x2 = normalize(x2)
    x3 = normalize(x3)

    Y = x1[:, 0, -6:-5]
    coords = x1[:, 0, -5:-3]
    X1 = x1[:, 1:, :]
    return X1, x2, x3, Y, coords


def train(x1, x2, x3, Y, coords, hP1, hP2, fname):
    db['Hyperparameters/' + fname] = (hP1.copy(), hP2.copy())
    model = Modulated_Relational(hP1, hP2)
    print(model.summary())
    hist = model.fit([x1, x2, x3, coords],
                     Y,
                     epochs=50,
                     batch_size=512,
                     verbose=1)
    pred = model.predict([x1[:1000], x2[:1000], x3[:1000], coords[:1000]])
    for p in range(len(pred)):
        print(pred[p], Y[p], pred[p] - Y[p])
    model.save_weights('DB/Weights/' + fname)
    db['Hist/' + fname] = hist.history
    return


def main():
    x1, x2, x3, Y, coords = normalization()
    for i in range(1, 10):
        size1 = np.random.randint(1, 5)
        LS1 = np.random.randint(1, 10, size1)*10
        hP1 = {}
        hP1['layer_size'] = LS1
        hP1['name'] = 'F1'
        hP1['N_layers'] = len(hP1['layer_size'])
        hP1['activations'] = [LeakyReLU(0.3)]*(len(hP1['layer_size']) - 1) + ['linear']
        hP1['dropout'] = ['True']*len(hP1['layer_size'])
        size2 = np.random.randint(0, 4)
        LS2 = np.random.randint(1, 10, size2)*10
        hP2 = {}
        hP2['layer_size'] = LS2
        hP2['name'] = 'G1'
        hP2['N_layers'] = len(hP2['layer_size'])
        hP2['activations'] = [LeakyReLU(0.3)]*(len(hP2['layer_size']) - 1) + ['linear']
        hP2['dropout'] = ['True']*hP2['N_layers']

        fname = '/params_' + str(i)
        print('')
        print('Beginning to train model with the following hyperparameters:')
        print('Relational Level 1:')
        for k in hP1:
            print('\t', k, '=', hP1[k])
        print('')
        print('Relational Level 2:')
        for k in hP2:
            print('\t', k, '=', hP2[k])
        try:
            train(x1, x2, x3, Y, coords, hP1, hP2, fname)
        except:
            continue
    return


main()

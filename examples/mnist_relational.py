import keras
from pylation import MLP
from pylation import Relational
from keras.datasets import mnist
from keras.layers import Flatten
from keras.layers.advanced_activations import LeakyReLU
from keras.models import Model
from keras.layers import Input
import numpy as np


def main():
    num_classes = 10
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255
    print(x_train.shape, 'train samples')
    print(x_test.shape, 'test samples')

    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)

    LS1 = np.asarray([32])
    LS2 = np.asarray([32])

    size1 = len(LS1)
    size2 = len(LS2)

    hyperparams1_0 = {
                    'layer_size': sorted(LS1, reverse=True),
                    'N_layers': size1,
                    'activations': [LeakyReLU(0.3)]*(size1),
                    'dropout': True,
                    'L1': 0.0,
                    'L2': 0.0,
                    'timedistributed': True,
                    }

    hyperparams1_1 = {
                    'layer_size': sorted(LS2, reverse=True),
                    'N_layers': size2,
                    'activations': [LeakyReLU(0.3)]*(size2),
                    'dropout': True,
                    'L1': 0.0,
                    'L2': 0.0,
                    'timedistributed': True,
                    }

    hyperparams3 = {
                    'layer_size': [256, 10],
                    'N_layers': 2,
                    'activations': ['relu', 'softmax'],
                    'dropout': False,
                    'L1': 0.0,
                    'L2': 0.0,
                    'timedistributed': False,
                    }

    hyperparams = {'hyperparams1': hyperparams1_0,
                   'hyperparams2': hyperparams1_1}

    A = Input(x_train.shape[1:])

    AA = Relational(A, A, **hyperparams)
    out = Flatten()(AA)

    final = MLP(out, **hyperparams3)

    model = Model(inputs=[A],
                  outputs=[final])
    model.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    print(model.summary())
    model.fit([x_train],
              y_train,
              epochs=10,
              batch_size=128,
              verbose=1,
              validation_data=(x_test, y_test))

    return model


if __name__ == '__main__':
    main()

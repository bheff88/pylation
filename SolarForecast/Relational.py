import numpy as np
from keras.layers.advanced_activations import LeakyReLU
from keras.models import Model
from keras.layers import Dense, Dropout, Flatten, Input, Lambda, \
                Concatenate, Reshape, Dot, TimeDistributed, Add, Average
from keras import backend as K


class Module:
    '''
    Creates an MLP model to be used within the Relational Network:
        Input:  Dictionary of Hyperparameters
        Output: When moduleOut is called, returns the MLP
    '''

    def __init__(self, hP):
        self.layers = hP['N_layers']
        self.activations = hP['activations']
        self.sizes = hP['layer_size']
        self.name = hP['name']
        self.module = []
        self.dropout = hP['dropout']
        for i in range(self.layers):
            tmp = TimeDistributed(Dense(self.sizes[i],
                                        activation=self.activations[i]),
                                  name=self.name + '_' + str(i))
            self.module.append(tmp)
            if self.dropout[i]:
                tmp = Dropout(0.3)
                self.module.append(tmp)

    def moduleOut(self, data):
        for layer in self.module:
            data = layer(data)
        return data


class Relational:
    '''
    Creates a fully connected Relational Network that can be used as if it were
    a built in keras layer. The only difference here are how the user specifies
    the hyperparameters of the models to be tested.
    '''

    def __init__(self, Oin):
        def make_Rs_Rr(n):
            Rr = np.identity(n)
            Rr = np.repeat(Rr, n, axis=1)
            Rs = np.identity(n).reshape(1, n, n)
            Rs = np.repeat(Rs, n, axis=0)
            Rs = Rs.reshape(n**2, n).T
            return Rr, Rs

        self.arr = []
        self.concat = Concatenate()
        self.concat2 = Concatenate(axis=1)
        self.Oin = Oin
        self.dims = self.Oin.shape
        Rr, Rs = make_Rs_Rr(int(self.dims[1]))
        self.receiver = Rr
        self.sender = Rs
        self.b = np.zeros(int(self.dims[1])**2)
        self.In = Input((self.dims[1:]))
        self.Rr = Dense(int(self.dims[1])**2, use_bias=False)
        self.Rr.trainable = False
        self.Rs = Dense(int(self.dims[1])**2, use_bias=False)
        self.Rs.trainable = False
        self.relations = []

    def permutate(self):
        def transpose_3tensor(t):
            return K.permute_dimensions(t, (0, 2, 1))
        T = Lambda(transpose_3tensor)
        Oin = self.In
        O1 = T(Oin)
        O2 = T(Oin)
        r = self.Rr(O1)
        r = T(r)
        s = self.Rs(O2)
        s = T(s)
        out = Concatenate(axis=-1)([r, s])
        relations = Model(inputs=Oin, outputs=out)
        relations.set_weights([self.receiver, self.sender])
        return relations(self.Oin)

    def recombine(self, t):
        def sums(t):
            return K.sum(t, axis=1)
        Sum = Lambda(sums)
        out = Reshape((int(self.dims[1]),
                       int(self.dims[1]),
                       int(t.shape[-1])))(t)
        out = Sum(out)
        out = Concatenate(axis=-1)([self.Oin, out])

        return out

    def Run(self, hP1, hP2):
        F_in = self.permutate()
        module1 = Module(hP1)
        module2 = Module(hP2)
        Fout = module1.moduleOut(F_in)
        E = self.recombine(Fout)
        gout = module2.moduleOut(E)
        return gout


def Modulated_Relational(hP1, hP2):
    '''
    This takes the Relational Network one step further by creating a modulated
    Relational network that essentially wraps a Relational Network
    around three smaller Relational Networks
    '''

    def customLoss(yTrue, yPred):
        T_m = K.mean(yTrue)
        yTrue = yTrue + T_m
        P_m = K.mean(yPred)
        yPred = yPred + P_m

        P_dev = K.sqrt(K.sum((yPred - P_m) ** 2)/64)
        T_dev = K.sqrt(K.sum((yTrue - T_m) ** 2)/64)

        P_k = K.sum(((yPred - P_m) ** 4))/(64 * P_dev**4)
        T_k = K.sum(((yTrue - T_m) ** 4))/(64 * T_dev**4)

        mse = K.mean((100*yPred - 100*yTrue)**2)
        kurt = (P_k - T_k)**2

        return mse + kurt

    Data1 = Input((14, 17,))
    Data2 = Input((14, 17,))
    Data3 = Input((14, 17,))
    coords = Input((2,))

    Rel = Relational(Data1)
    Rel2 = Relational(Data2)
    Rel3 = Relational(Data3)

    out1 = Rel.Run(hP1, hP2)

    hP1['name'] = 'F2'
    hP2['name'] = 'G2'

    out2 = Rel2.Run(hP1, hP2)

    hP1['name'] = 'F3'
    hP2['name'] = 'G3'

    out3 = Rel3.Run(hP1, hP2)

    def sums(t):
        return K.sum(t, axis=1)

    Sum = Lambda(sums)

    Rout1 = Sum(out1)
    Rout2 = Sum(out2)
    Rout3 = Sum(out3)

    out = Concatenate(1)([Rout1, Rout2, Rout3])
    out = Reshape((1, int(out.shape[-1])//1))(Rout1)
    out = Sum(out)

    final = Dense(90, activation=LeakyReLU(0.3))(Rout1)
    final = Dropout(0.3)(final)
    final = Dense(90, activation=LeakyReLU(0.3))(final)
    final = Dropout(0.3)(final)
    final = Dense(10, activation=LeakyReLU(0.3))(final)
    final = Dense(1, activation='linear')(final)

    model = Model(inputs=[Data1, Data2, Data3, coords],
                  outputs=[final])
    model = Model(inputs=[Data1, coords],
                  outputs=[final])
    model.compile('adam', customLoss)
    return model

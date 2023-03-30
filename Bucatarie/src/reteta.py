import pickle
import os
class Reteta:
    def __init__(self, nume):
        self.nume = nume
        self.reteta = {}


    def retetaAleasa(self, numeReteta):
        # alegem reteta si facem load la ingredientele din fisier in dictionarul reteta.
        filename = 'data/' + numeReteta + '.pickle'
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                content = pickle.load(f)
                for element in content:
                    l = element.split(' ')
                    self.reteta[l[0]] = int(l[1])
        else:
            print(f"Reteta dorita {numeReteta} nu exista in bucataria dumneavoastra")

    def printReteta(self, numeReteta):
        self.retetaAleasa(numeReteta)
        print(self.reteta)
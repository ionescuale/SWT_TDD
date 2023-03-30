import pickle
class Reteta:
    def __init__(self, nume):
        self.nume = nume
        self.reteta = {}


    def retetaAleasa(self, numeReteta):
        # alegem reteta si facem load la ingredientele din fisier in dictionarul reteta.
        filename = 'data/' + numeReteta + '.pickle'
        with open(filename, 'rb') as f:
            content = pickle.load(f)
            for element in content:
                l = element.split(' ')
                self.reteta[l[0]] = int(l[1])
        print(self.reteta)
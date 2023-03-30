

class Reteta:
    def __init__(self, nume):
        self.nume = nume
        self.reteta = {}


    def reteta(self, numeReteta):
        filename = 'data/' + numeReteta + '.pickle'
        with open(filename, 'rb') as f:
            a = pickle.load(f)
            self.reteta.update(a)
            print(reteta)
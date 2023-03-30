class Reteta:
    def __init__(self, nume):
        self.nume = nume
        self.reteta = {}


    def retetaAleasa(self, numeReteta):
        # alegem reteta si facem load la ingredientele din fisier in dictionarul reteta.
        filename = 'data/' + numeReteta + '.pickle'
        with open(filename, 'rb') as f:
            line = pickle.load(f)
            self.reteta.update(line)
            print(self.reteta)
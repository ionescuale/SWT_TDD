from src.reteta import Reteta

class ProdusFinal(Reteta):

    def createProduct(self, numeReteta):
        filename = 'data/' + numeReteta + '.pickle'
        with open(filename, 'rb') as f:
            a = pickle.load(f)
            print(a)

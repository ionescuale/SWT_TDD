import pickle

class Bucatarie:
    def __init__(self, nume):
        self.nume = nume
        self.inventar = {}


    def storeInFile(self):
        with open('inventar.pickle', 'wb') as f:
            pickle.dump(self.inventar, f)


    def loadFromFile(self):
        with open('inventar.pickle', 'rb') as f:
            ingredient = pickle.load(f)
            self.inventar.update(ingredient)


    def arataInventar(self):
        self.loadFromFile()
        print(self.inventar)


    def adaugaIngredient(self, ingredient, cantitate):
        self.loadFromFile()
        if ingredient in self.inventar.keys():
            self.inventar[ingredient] += cantitate
        else:
            self.inventar[ingredient] = cantitate
        self.storeInFile()


    def scadeInventar(self, ingredient, cantitate):
        # scade din inventar elementele necesare unei retete, dupa ce se face produs final
        self.loadFromFile()
        if ingredient in self.inventar.keys():
            if cantitate <= self.inventar[ingredient]:
                self.inventar[ingredient] -= cantitate
                self.storeInFile()
            else:
                print(f'Nu aveti cantitatea suficienta de {ingredient}')
        else:
            print("Produsul nu exista in inventar")


    def creeazaReteta(self, numeReteta, lista):
        reteta = lista
        filename = 'data/' + numeReteta + '.pickle'
        with open(filename, 'wb') as f:
            pickle.dump(reteta, f)

from bucatarie import Bucatarie
from reteta import Reteta

class ProdusFinal(Reteta):
    def __init__(self):
        Reteta.__init__(self, nume)


    def createProduct(self, numeReteta):
        # alegem o reteta si verificam daca ingredientele retetei sunt in inventar.
        # daca ingredientele sunt in inventar le scadem din inventar
        # salvam n flag care ne spune daca am avut ingrediente care nu au fost gasite in inventar, sau nu era cantitate suficienta
        # daca flagul este pe true, atunci facem update si in fisiserul inventar, cconsiderand ca produsul final a fost facut
        self.retetaAleasa(numeReteta)
        flag_updateInventar = True
        for item in self.reteta.items():
            if item in self.inventar.items():
                if self.reteta[item] <= self.inventar[item]:
                    self.Bucatarie.scadeInventar(item, self.reteta[item])
                else:
                    print(f'Nu aveti cantitatea suficienta de {item}')
                    flag_updateInventar = False
                    break
            else:
                print(f'Nu aveti ingredientul {item} in inventar')
                flag_updateInventar = False
                break
        if flag_updateInventar == True:
            Bucatarie.storeInFile()
            print(f'produsul {numeReteta} a fost creat cu succes!')
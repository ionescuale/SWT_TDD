from src.bucatarie import Bucatarie
from src.produsfinal import ProdusFinal
from src.reteta import Reteta

a = Bucatarie("Alexandra")

request = eval(input("Alegeti:\n "
                     "1 - Vizualizare inventar \n "
                     "2 - Adaugati in inventar din lista de cumparaturi\n "
                     "3 - Adaugati in inventar ingrediente manual\n "
                     "4 - Adaugati o reteta\n"
                     ">>>"))
# vizualizarea inventarului
if request == 1:
    a.arataInventar()

# Adaugam in inventar din lista de cumparaturi
elif request == 2:
    listaCumparaturi = input("Intoduceti lista sub format 'file.txt'\n>>>")
    cale = "data/"+listaCumparaturi
    with open(cale, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            l = line.split(' ')
            a.adaugaIngredient(l[0], int(l[1]))

# Adaugam in inventar ingrediente manual
elif request == 3:
    ingredientCantitate = ' '
    while ' ' in ingredientCantitate:
        ingredientCantitate = input("Intoduceti ingredientul si cantiatatea exprimata in grame, sau nr de bucati\n >>>")
        l = ingredientCantitate.split(' ')
        if len(l) == 2:
            a.adaugaIngredient(l[0], int(l[1]))
        else:
            print("Am terminat adaugarea ingredientelor.")

# Definim o reteta
elif request == 4:
    numeReteta = input("Introduceti numele retetei\n>>>")
    numarIngrediente = eval(input("Introduceti nr de ingrediente\n>>>"))
    print("Intoduceti ingredientul si cantiatatea exprimata in grame, sau nr de bucati:")
    l = []
    for i in range(numarIngrediente):
        ingredientCantitate = input(">>>")
        l.append(ingredientCantitate)
        a.creeazaReteta(numeReteta, l)
    print("Reteta pentru clatite a fost adaugata cu succes!")
else:
    pass


# a.creeazaReteta("Clatite", [("faina", 200), ("oua", 4), ("lapte", 200)])

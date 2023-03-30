import pickle
def test_verificare_fisier():
    nume_fisier = 'C:\Users\alexandra.ionescu\Desktop\CursPythonSDA\SWT_TDD\Bucatarie\data\inventar.pickle'
    with open(nume_fisier, 'rb') as f:
        continut = pickle.load(f)
    print(continut)
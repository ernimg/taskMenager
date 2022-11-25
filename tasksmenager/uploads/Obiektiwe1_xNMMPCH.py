#  tworzenie klasy 
class Drzewo:
    nazwa  = 'sosna'
    wiek = 40
    wysokosc = 14

drzewo1 = Drzewo()

# tworzenie nowych pol dla instancji 

drzewo1.cena = '100zł'


print(dir(drzewo1))
print(dir(Drzewo))

# parametr self

class Drzewa:
    def wyswietl_info_o_drzewie(self):
        pass



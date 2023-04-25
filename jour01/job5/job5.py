class Animal:
    def __init__(self):
        self.age = 0
        self.nom = ""

    def vieillir(self):
        self.age += 1


mon_animal = Animal()

print("L'age de l'animal est {} ans".format(mon_animal.age))

mon_animal.vieillir()

print("L'age de l'animal est {} ans".format(mon_animal.age))
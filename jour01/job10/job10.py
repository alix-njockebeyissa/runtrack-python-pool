class Voiture:
    def __init__(self, marque, modele, annee, kilometre, en_marche=False, reservoir=50):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometre = kilometre
        self.en_marche = en_marche
        self.reservoir = reservoir

    def get_marque(self):
        return self.marque

    def set_marque(self, marque):
        self.marque = marque

    def get_modele(self):
        return self.modele

    def set_modele(self, modele):
        self.modele = modele

    def get_annee(self):
        return self.annee

    def set_annee(self, annee):
        self.annee = annee

    def get_kilometre(self):
        return self.kilometre

    def set_kilometre(self, kilometre):
        self.kilometre = kilometre

    def get_en_marche(self):
        return self.en_marche

    def set_en_marche(self, en_marche):
        self.en_marche = en_marche

    def verifier_plein(self):
        return self.reservoir

    def demarrer(self):
        if self.reservoir > 5:
            self.en_marche = True
            print("Voiture démarré !")
        else :
            print("Impossible de démarré !")

    def arret(self):
        self.en_marche = False

voiture = Voiture("Renault", "Clio", 2020, 10000)
print("Marque :", voiture.marque)
print("Modèle :", voiture.modele)
print("Année :", voiture.annee)
print("Kilométrage :", voiture.kilometre)
print("En marche :", voiture.en_marche)
print("Niveau de carburant :", voiture.reservoir)
voiture.demarrer()
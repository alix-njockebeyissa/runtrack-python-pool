class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__emprunte = False

    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Erreur : le nombre de pages doit être un nombre entier positif.")

    def est_emprunte(self):
        return self.__emprunte

    def emprunter(self):
        if self.est_emprunte():
            print("Le livre est déjà emprunté.")
        else:
            self.__emprunte = True
            print("Le livre a été emprunté.")

    def rendre(self):
        if not self.est_emprunte():
            print("Le livre n'a pas été emprunté.")
        else:
            self.__emprunte = False
            print("Le livre a été rendu.")


mon_livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 100)

print("Le livre est emprunté : ", mon_livre)
class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
    def SePresenter(self):
        return "Je suis " + self.nom + " " + self.prenom

personne1 = Personne("John", "Doe")
personne2 = Personne("Jean", "Dupon")

print(personne1.SePresenter()) # Output: "Je suis John Doe"
print(personne2.SePresenter()) # Output: "Je suis Jean Dupon"
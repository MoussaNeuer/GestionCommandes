# Classe représentant un fournisseur

class Fournisseur:

    def __init__(self, id=None, code="", raison_sociale="",
                 email="", telephone="", adresse="", date_creation=None):
        self.id = id
        self.code = code
        self.raison_sociale = raison_sociale
        self.email = email
        self.telephone = telephone
        self.adresse = adresse
        self.date_creation = date_creation

    def __str__(self):
        return f"[{self.id}] {self.code} - {self.raison_sociale} | {self.email} | Tél: {self.telephone}"

    def afficher(self):
        print(f"ID            : {self.id}")
        print(f"Code          : {self.code}")
        print(f"Raison sociale: {self.raison_sociale}")
        print(f"Email         : {self.email}")
        print(f"Téléphone     : {self.telephone}")
        print(f"Adresse       : {self.adresse}")
        print(f"Date création : {self.date_creation}")

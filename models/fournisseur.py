# Classe représentant un fournisseur

class Fournisseur:
    
    def __init__(self, id, code, raison_sociale, email, telephone, adresse, date_creation):
        self.id = id
        self.code = code
        self.raison_sociale = raison_sociale
        self.email = email
        self.telephone = telephone
        self.adresse = adresse
        self.date_creation = date_creation

    def __str__(self):
        return f"[{self.id}] {self.code} - {self.raison_sociale} | {self.email} | Tél: {self.telephone}"
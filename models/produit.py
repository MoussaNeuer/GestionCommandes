# Classe représentant un produit

class Produit:

    def __init__(self, id=None, reference="", designation="",
                 prix_unitaire=0.0, stock=0, date_creation=None):
        self.id = id
        self.reference = reference
        self.designation = designation
        self.prix_unitaire = prix_unitaire
        self.stock = stock
        self.date_creation = date_creation

    def __str__(self):
        return f"[{self.id}] {self.reference} - {self.designation} | Prix: {self.prix_unitaire} FCFA | Stock: {self.stock}"

    def afficher(self):
        print(f"ID            : {self.id}")
        print(f"Référence     : {self.reference}")
        print(f"Désignation   : {self.designation}")
        print(f"Prix unitaire : {self.prix_unitaire} FCFA")
        print(f"Stock         : {self.stock}")
        print(f"Date création : {self.date_creation}")

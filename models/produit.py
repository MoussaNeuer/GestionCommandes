# Classe représentant un produit

class Produit:

    def __init__(self, id, reference, designation, prix_unitaire, stock, date_creation):
        self.id = id
        self.reference = reference
        self.designation = designation
        self.prix_unitaire = prix_unitaire
        self.stock = stock
        self.date_creation = date_creation

    def __str__(self):
        return f"[{self.id}] {self.reference} - {self.designation} | Prix: {self.prix_unitaire} FCFA | Stock: {self.stock}"
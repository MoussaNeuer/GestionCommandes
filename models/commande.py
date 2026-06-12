# Classe représentant une commande et ses lignes

class LigneCommande:

    def __init__(self, id, commande_id, produit_id, quantite, prix_unitaire):
        self.id = id
        self.commande_id = commande_id
        self.produit_id = produit_id
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire

    def sous_total(self):
        # calcule le montant de cette ligne
        return self.quantite * self.prix_unitaire

    def __str__(self):
        return f"  Produit #{self.produit_id} | Qté: {self.quantite} x {self.prix_unitaire} FCFA = {self.sous_total()} FCFA"


class Commande:

    def __init__(self, id, numero, date_commande, fournisseur_id, montant_total, statut, date_creation):
        self.id = id
        self.numero = numero
        self.date_commande = date_commande
        self.fournisseur_id = fournisseur_id
        self.montant_total = montant_total
        self.statut = statut
        self.date_creation = date_creation

    def __str__(self):
        return f"[{self.id}] {self.numero} | Fournisseur #{self.fournisseur_id} | Statut: {self.statut} | Total: {self.montant_total} FCFA"
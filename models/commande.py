# Classe représentant une ligne de commande (un produit dans une commande)

class LigneCommande:

    def __init__(self, id=None, commande_id=None, produit_id=None,
                 quantite=0, prix_unitaire=0.0):
        self.id = id
        self.commande_id = commande_id
        self.produit_id = produit_id
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire

    def sous_total(self):
        # Calcule le montant de cette ligne
        return self.quantite * self.prix_unitaire

    def __str__(self):
        return f"  Produit #{self.produit_id} | Qté: {self.quantite} x {self.prix_unitaire} FCFA = {self.sous_total()} FCFA"


# Classe représentant une commande fournisseur

class Commande:

    def __init__(self, id=None, numero="", date_commande=None,
                 fournisseur_id=None, montant_total=0.0,
                 statut="EN_ATTENTE", date_creation=None):
        self.id = id
        self.numero = numero
        self.date_commande = date_commande
        self.fournisseur_id = fournisseur_id
        self.montant_total = montant_total
        self.statut = statut
        self.date_creation = date_creation

    def __str__(self):
        return (f"[{self.id}] {self.numero} | Fournisseur #{self.fournisseur_id} "
                f"| Statut: {self.statut} | Total: {self.montant_total} FCFA")

    def afficher(self):
        print(f"ID            : {self.id}")
        print(f"Numéro        : {self.numero}")
        print(f"Date commande : {self.date_commande}")
        print(f"Fournisseur   : #{self.fournisseur_id}")
        print(f"Montant total : {self.montant_total} FCFA")
        print(f"Statut        : {self.statut}")
        print(f"Date création : {self.date_creation}")

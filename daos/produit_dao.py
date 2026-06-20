from models.produit import Produit
from database.connexion import DatabaseConnection

class ProduitDAO:
    # Ajouter un produit
    def ajouter_produit(self, produit):
        db = DatabaseConnection()
        if not db.connect():
            print("Pas de connection")
            return False
        sql = """
        INSERT INTO produit(reference, designation, prix_unitaire, stock)
        VALUES (%s, %s, %s, %s)
        """
        params = (produit.reference, produit.designation, produit.prix_unitaire, produit.stock)
        ok = db.execute(sql, params)
        if ok:
            db.commit()
        db.disconnect()
        return ok

    # Lister tous les produits
    def lister_produit(self):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "SELECT * FROM produit"
        db.execute(sql)
        resultats = db.fetchall()
        db.disconnect()
        produits = []
        for ligne in resultats:
            produit = Produit(
                id=ligne[0],
                reference=ligne[1],
                designation=ligne[2],
                prix_unitaire=ligne[3],
                stock=ligne[4],
                date_creation=ligne[5]
            )
            produits.append(produit)
        return produits

    # Rechercher un produit par désignation
    def rechercher_produit(self, mot_cle):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "SELECT * FROM produit WHERE designation = %s or reference = %s"
        params = (mot_cle, mot_cle,)
        db.execute(sql, params)
        ligne = db.fetchone()
        db.disconnect()
        if ligne:
            return Produit(*ligne)
        return None

    # Supprimer un produit
    def supprimer_produit(self, id_produit):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "DELETE FROM produit WHERE id=%s"
        params = (id_produit,)
        ok = db.execute(sql, params)
        if ok:
            db.commit()
        db.disconnect()
        return ok

    # Modifier un produit
    def modifier_produit(self, produit):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = """
        UPDATE produit
        SET reference=%s, designation=%s, prix_unitaire=%s, stock=%s
        WHERE id = %s
        """
        params = (produit.reference, produit.designation, produit.prix_unitaire,
                   produit.stock, produit.id)
        ok = db.execute(sql, params)
        if ok:
            db.commit()
        db.disconnect()
        return ok

    # Trouver le produit par son ID
    def get_by_id(self, id_produit):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "SELECT * FROM produit WHERE id = %s"
        params = (id_produit,)
        db.execute(sql, params)
        ligne = db.fetchone()
        db.disconnect()
        if ligne:
            return Produit(
                id=ligne[0],
                reference=ligne[1],
                designation=ligne[2],
                prix_unitaire=ligne[3],
                stock=ligne[4],
                date_creation=ligne[5]
            )
        return None

    # Compter le nombre de lignes de commande pour ce produit (pour la suppression)
    def compter_lignes_commande(self, id_produit):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "SELECT COUNT(*) FROM ligne_commande WHERE produit_id = %s"
        params = (id_produit,)
        db.execute(sql, params)
        ligne = db.fetchone()
        db.disconnect()
        return ligne[0]

    # Liste des produits dont le stock est inférieur au seuil
    def produits_stock_faible(self, seuil):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "SELECT * FROM produit WHERE stock < %s"
        params = (seuil,)
        db.execute(sql, params)
        resultats = db.fetchall()
        db.disconnect()
        produits = []
        for ligne in resultats:
            produit = Produit(
                id=ligne[0],
                reference=ligne[1],
                designation=ligne[2],
                prix_unitaire=ligne[3],
                stock=ligne[4],
                date_creation=ligne[5]
            )
            produits.append(produit)
        return produits

    # Mettre à jour uniquement le stock (utilisé après une commande)
    def mettre_a_jour_stock(self, id_produit, nouveau_stock):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "UPDATE produit SET stock = %s WHERE id = %s"
        params = (nouveau_stock, id_produit)
        ok = db.execute(sql, params)
        if ok:
            db.commit()
        db.disconnect()
        return ok

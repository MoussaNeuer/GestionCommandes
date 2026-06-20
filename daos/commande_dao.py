from models.commande import Commande, LigneCommande
from database.connexion import DatabaseConnection

class CommandeDAO:
    # Ajouter une commande (sans les lignes)
    def ajouter_commande(self, commande):
        db = DatabaseConnection()
        if not db.connect():
            print("Pas de connection")
            return False
        sql = """
        INSERT INTO commande(numero, fournisseur_id, montant_total, statut)
        VALUES (%s, %s, %s, %s)
        """
        params = (commande.numero, commande.fournisseur_id, commande.montant_total, commande.statut)
        ok = db.execute(sql, params)
        if ok:
            db.commit()
        db.disconnect()
        return ok

    # Lister toutes les commandes
    def lister_commande(self):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "SELECT * FROM commande"
        db.execute(sql)
        resultats = db.fetchall()
        db.disconnect()
        commandes = []
        for ligne in resultats:
            commande = Commande(
                id=ligne[0],
                numero=ligne[1],
                date_commande=ligne[2],
                fournisseur_id=ligne[3],
                montant_total=ligne[4],
                statut=ligne[5],
                date_creation=ligne[6]
            )
            commandes.append(commande)
        return commandes

    # Rechercher une commande par numéro
    def rechercher_commande(self, numero):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "SELECT * FROM commande WHERE numero = %s"
        params = (numero,)
        db.execute(sql, params)
        ligne = db.fetchone()
        db.disconnect()
        if ligne:
            return Commande(*ligne)
        return None

    # Supprimer une commande
    def supprimer_commande(self, id_commande):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "DELETE FROM commande WHERE id=%s"
        params = (id_commande,)
        ok = db.execute(sql, params)
        if ok:
            db.commit()
        db.disconnect()
        return ok

    # Modifier le statut d'une commande
    def modifier_statut(self, id_commande, statut):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "UPDATE commande SET statut=%s WHERE id = %s"
        params = (statut, id_commande)
        ok = db.execute(sql, params)
        if ok:
            db.commit()
        db.disconnect()
        return ok

    # Mettre à jour le montant total d'une commande
    def modifier_montant(self, id_commande, montant_total):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "UPDATE commande SET montant_total=%s WHERE id = %s"
        params = (montant_total, id_commande)
        ok = db.execute(sql, params)
        if ok:
            db.commit()
        db.disconnect()
        return ok

    # Trouver une commande par son ID
    def get_by_id(self, id_commande):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "SELECT * FROM commande WHERE id = %s"
        params = (id_commande,)
        db.execute(sql, params)
        ligne = db.fetchone()
        db.disconnect()
        if ligne:
            return Commande(
                id=ligne[0],
                numero=ligne[1],
                date_commande=ligne[2],
                fournisseur_id=ligne[3],
                montant_total=ligne[4],
                statut=ligne[5],
                date_creation=ligne[6]
            )
        return None

    # Récupérer le dernier ID inséré (pour connaître l'ID de la commande créée)
    def get_dernier_id(self):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "SELECT LAST_INSERT_ID()"
        db.execute(sql)
        ligne = db.fetchone()
        db.disconnect()
        return ligne[0]

    # Liste des commandes d'un fournisseur
    def commandes_du_fournisseur(self, id_fournisseur):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "SELECT * FROM commande WHERE fournisseur_id = %s"
        params = (id_fournisseur,)
        db.execute(sql, params)
        resultats = db.fetchall()
        db.disconnect()
        commandes = []
        for ligne in resultats:
            commande = Commande(
                id=ligne[0],
                numero=ligne[1],
                date_commande=ligne[2],
                fournisseur_id=ligne[3],
                montant_total=ligne[4],
                statut=ligne[5],
                date_creation=ligne[6]
            )
            commandes.append(commande)
        return commandes

    # Liste des commandes en attente
    def commandes_en_attente(self):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "SELECT * FROM commande WHERE statut = 'EN_ATTENTE'"
        db.execute(sql)
        resultats = db.fetchall()
        db.disconnect()
        commandes = []
        for ligne in resultats:
            commande = Commande(
                id=ligne[0],
                numero=ligne[1],
                date_commande=ligne[2],
                fournisseur_id=ligne[3],
                montant_total=ligne[4],
                statut=ligne[5],
                date_creation=ligne[6]
            )
            commandes.append(commande)
        return commandes

    # Chiffre d'affaires total (commandes validées et livrées)
    def chiffre_affaires(self):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "SELECT SUM(montant_total) FROM commande WHERE statut = 'VALIDEE' or statut = 'LIVREE'"
        db.execute(sql)
        ligne = db.fetchone()
        db.disconnect()
        if ligne[0] is None:
            return 0
        return ligne[0]


class LigneCommandeDAO:
    # Ajouter une ligne de commande
    def ajouter_ligne(self, ligne_commande):
        db = DatabaseConnection()
        if not db.connect():
            print("Pas de connection")
            return False
        sql = """
        INSERT INTO ligne_commande(commande_id, produit_id, quantite, prix_unitaire)
        VALUES (%s, %s, %s, %s)
        """
        params = (ligne_commande.commande_id, ligne_commande.produit_id,
                   ligne_commande.quantite, ligne_commande.prix_unitaire)
        ok = db.execute(sql, params)
        if ok:
            db.commit()
        db.disconnect()
        return ok

    # Lister les lignes d'une commande
    def lister_lignes(self, id_commande):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "SELECT * FROM ligne_commande WHERE commande_id = %s"
        params = (id_commande,)
        db.execute(sql, params)
        resultats = db.fetchall()
        db.disconnect()
        lignes = []
        for ligne in resultats:
            lc = LigneCommande(
                id=ligne[0],
                commande_id=ligne[1],
                produit_id=ligne[2],
                quantite=ligne[3],
                prix_unitaire=ligne[4]
            )
            lignes.append(lc)
        return lignes

    # Top 5 des produits les plus commandés
    def top5_produits(self):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = """
        SELECT produit_id, SUM(quantite) AS total_quantite
        FROM ligne_commande
        GROUP BY produit_id
        ORDER BY total_quantite DESC
        LIMIT 5
        """
        db.execute(sql)
        resultats = db.fetchall()
        db.disconnect()
        return resultats

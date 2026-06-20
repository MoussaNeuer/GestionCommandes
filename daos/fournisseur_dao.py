from models.fournisseur import Fournisseur
from database.connexion import DatabaseConnection

class FournisseurDAO:
    # Ajouter un fournisseur
    def ajouter_fournisseur(self, fournisseur):
        db = DatabaseConnection()
        if not db.connect():
            print("Pas de connection")
            return False
        sql = """
        INSERT INTO fournisseur(code, raison_sociale, email, telephone, adresse)
        VALUES (%s, %s, %s, %s, %s)
        """
        params = (fournisseur.code, fournisseur.raison_sociale, fournisseur.email,
                   fournisseur.telephone, fournisseur.adresse)
        ok = db.execute(sql, params)
        if ok:
            db.commit()
        db.disconnect()
        return ok

    # Lister tous les fournisseurs
    def lister_fournisseur(self):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "SELECT * FROM fournisseur"
        db.execute(sql)
        resultats = db.fetchall()
        db.disconnect()
        fournisseurs = []
        for ligne in resultats:
            fournisseur = Fournisseur(
                id=ligne[0],
                code=ligne[1],
                raison_sociale=ligne[2],
                email=ligne[3],
                telephone=ligne[4],
                adresse=ligne[5],
                date_creation=ligne[6]
            )
            fournisseurs.append(fournisseur)
        return fournisseurs

    # Rechercher un fournisseur (code ou raison sociale)
    def rechercher_fournisseur(self, mot_cle):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "SELECT * FROM fournisseur WHERE code = %s or raison_sociale = %s"
        params = (mot_cle, mot_cle,)
        db.execute(sql, params)
        ligne = db.fetchone()
        db.disconnect()
        if ligne:
            return Fournisseur(*ligne)
        return None

    # Supprimer un fournisseur
    def supprimer_fournisseur(self, id_fournisseur):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "DELETE FROM fournisseur WHERE id=%s"
        params = (id_fournisseur,)
        ok = db.execute(sql, params)
        if ok:
            db.commit()
        db.disconnect()
        return ok

    # Modifier un fournisseur
    def modifier_fournisseur(self, fournisseur):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = """
        UPDATE fournisseur
        SET code=%s, raison_sociale=%s, email=%s, telephone=%s, adresse=%s
        WHERE id = %s
        """
        params = (fournisseur.code, fournisseur.raison_sociale, fournisseur.email,
                   fournisseur.telephone, fournisseur.adresse, fournisseur.id)
        ok = db.execute(sql, params)
        if ok:
            db.commit()
        db.disconnect()
        return ok

    # Trouver le fournisseur par son ID
    def get_by_id(self, id_fournisseur):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "SELECT * FROM fournisseur WHERE id = %s"
        params = (id_fournisseur,)
        db.execute(sql, params)
        ligne = db.fetchone()
        db.disconnect()
        if ligne:
            return Fournisseur(
                id=ligne[0],
                code=ligne[1],
                raison_sociale=ligne[2],
                email=ligne[3],
                telephone=ligne[4],
                adresse=ligne[5],
                date_creation=ligne[6]
            )
        return None

    # Compter le nombre de commandes d'un fournisseur (pour la suppression)
    def compter_commandes(self, id_fournisseur):
        db = DatabaseConnection()
        if not db.connect():
            return False
        sql = "SELECT COUNT(*) FROM commande WHERE fournisseur_id = %s"
        params = (id_fournisseur,)
        db.execute(sql, params)
        ligne = db.fetchone()
        db.disconnect()
        return ligne[0]

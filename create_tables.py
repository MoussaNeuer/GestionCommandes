"""
Script de création des tables MySQL.
À exécuter une seule fois avant de lancer l'application.
Utilise la classe DatabaseConnection (Singleton).
"""

from database.connexion import DatabaseConnection

# Ordre important : fournisseur et produit avant commande,
# commande avant ligne_commande (contraintes de clés étrangères)

TABLES = [
    (
        "fournisseur",
        """
        CREATE TABLE IF NOT EXISTS fournisseur (
            id             INT           NOT NULL AUTO_INCREMENT,
            code           VARCHAR(20)   NOT NULL,
            raison_sociale VARCHAR(100)  NOT NULL,
            email          VARCHAR(100)  NOT NULL,
            telephone      VARCHAR(20)   DEFAULT NULL,
            adresse        TEXT          DEFAULT NULL,
            date_creation  DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            UNIQUE KEY uq_fournisseur_code (code)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """
    ),
    (
        "produit",
        """
        CREATE TABLE IF NOT EXISTS produit (
            id             INT            NOT NULL AUTO_INCREMENT,
            reference      VARCHAR(20)    NOT NULL,
            designation    VARCHAR(150)   NOT NULL,
            prix_unitaire  DECIMAL(12,2)  NOT NULL CHECK (prix_unitaire > 0),
            stock          INT            NOT NULL DEFAULT 0 CHECK (stock >= 0),
            date_creation  DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            UNIQUE KEY uq_produit_reference (reference)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """
    ),
    (
        "commande",
        """
        CREATE TABLE IF NOT EXISTS commande (
            id             INT            NOT NULL AUTO_INCREMENT,
            numero         VARCHAR(20)    NOT NULL,
            date_commande  DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP,
            fournisseur_id INT            NOT NULL,
            montant_total  DECIMAL(14,2)  NOT NULL DEFAULT 0,
            statut         VARCHAR(20)    NOT NULL DEFAULT 'EN_ATTENTE',
            date_creation  DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            UNIQUE KEY uq_commande_numero (numero),
            CONSTRAINT chk_statut CHECK (statut IN ('EN_ATTENTE','VALIDEE','LIVREE','ANNULEE')),
            CONSTRAINT fk_commande_fournisseur
                FOREIGN KEY (fournisseur_id)
                REFERENCES fournisseur(id)
                ON DELETE RESTRICT
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """
    ),
    (
        "ligne_commande",
        """
        CREATE TABLE IF NOT EXISTS ligne_commande (
            id            INT           NOT NULL AUTO_INCREMENT,
            commande_id   INT           NOT NULL,
            produit_id    INT           NOT NULL,
            quantite      INT           NOT NULL CHECK (quantite > 0),
            prix_unitaire DECIMAL(12,2) NOT NULL CHECK (prix_unitaire > 0),
            PRIMARY KEY (id),
            CONSTRAINT fk_lc_commande
                FOREIGN KEY (commande_id)
                REFERENCES commande(id)
                ON DELETE CASCADE,
            CONSTRAINT fk_lc_produit
                FOREIGN KEY (produit_id)
                REFERENCES produit(id)
                ON DELETE RESTRICT
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """
    ),
]

def creer_tables():
    """Crée toutes les tables dans la base de données MySQL."""
    db = DatabaseConnection()

    # Connexion à la base de données
    if not db.connect():
        print("❌ Impossible de se connecter. Vérifiez database/config.py")
        return

    try:
        for nom_table, sql in TABLES:
            ok = db.execute(sql)
            if ok:
                print(f"   ✅ Table '{nom_table}' créée (ou déjà existante).")
            else:
                print(f"   ❌ Erreur lors de la création de la table '{nom_table}'.")

        db.commit()
        print("\n✅ Création des tables terminée avec succès !")

    except Exception as e:
        db.rollback()
        print(f"❌ Erreur inattendue : {e}")

    finally:
        db.disconnect()


if __name__ == "__main__":
    print("=" * 60)
    print("  CRÉATION DES TABLES MySQL - Gestion des Commandes")
    print("=" * 60)
    creer_tables()

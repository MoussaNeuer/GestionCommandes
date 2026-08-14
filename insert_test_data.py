"""
Script d'insertion de données de test pour MySQL/WAMP.
"""

from database.connexion import DatabaseConnection

FOURNISSEURS = [
    ("F001", "Technologie Dakar SARL",   "contact@techdk.sn",    "77 143 98 21", "Zone Industrielle, Dakar"),
    ("F002", "Informatique Express SN",  "info@infoexpress.sn",  "76 220 36 92", "Plateau, Dakar"),
    ("F003", "Global IT Sénégal",        "sales@globalit.sn",    "70 360 10 73", "Almadies, Dakar"),
    ("F004", "Bureau Plus Distribution", "bureau@bplus.sn",      "78 470 89 24", "Parcelles Assainies, Dakar"),
    ("F005", "Matériel Pro Afrique",     "mpro@mproa.sn",        "71 561 77 65", "Yoff, Dakar"),
]

PRODUITS = [
    ("REF001", "Ordinateur portable Dell Latitude 5540",  750000.00, 15),
    ("REF002", "Imprimante HP LaserJet Pro M404dn",       280000.00,  8),
    ("REF003", "Ecran Samsung 27 pouces FHD",             180000.00, 20),
    ("REF004", "Clavier mecanique Logitech MX Keys",       55000.00, 30),
    ("REF005", "Souris sans fil Microsoft Arc",            32000.00, 25),
    ("REF006", "Disque dur externe Seagate 2TB",           45000.00, 12),
    ("REF007", "Cable HDMI 2.0 - 2 metres",                3500.00,  3),
    ("REF008", "Switch reseau TP-Link 8 ports",            42000.00, 10),
    ("REF009", "Webcam Logitech C920 HD Pro",              65000.00,  5),
    ("REF010", "Casque audio Sony WH-1000XM5",            145000.00,  7),
    ("REF011", "Batterie externe Anker 20000 mAh",         28000.00, 18),
    ("REF012", "Adaptateur USB-C Hub 7-en-1",              22000.00,  4),
]

# (numero, index_fournisseur, statut, [(index_produit, quantite), ...])
COMMANDES = [
    ("CMD001", 0, "LIVREE",     [(0, 3), (2, 5)]),
    ("CMD002", 1, "VALIDEE",    [(1, 2), (3, 10), (4, 8)]),
    ("CMD003", 2, "EN_ATTENTE", [(5, 4), (6, 20)]),
    ("CMD004", 0, "EN_ATTENTE", [(7, 3), (8, 2)]),
    ("CMD005", 3, "ANNULEE",    [(9, 1), (10, 5)]),
    ("CMD006", 4, "LIVREE",     [(11, 6), (3, 15)]),
    ("CMD007", 1, "VALIDEE",    [(0, 2), (1, 1), (2, 3)]),
    ("CMD008", 2, "EN_ATTENTE", [(4, 10), (5, 6)]),
]


def inserer_donnees_test():
    """Insère toutes les données de test dans MySQL."""
    db = DatabaseConnection()
    if not db.connect():
        print("Erreur : Impossible de se connecter à la base.")
        return

    # On récupère la vraie connexion et le curseur depuis l'instance db
    connexion = db.connection
    curseur = db.cursor

    try:
        print("\n  1. Insertion des fournisseurs...")
        fournisseur_ids = []
        for code, rs, email, tel, adresse in FOURNISSEURS:
            curseur.execute(
                "INSERT INTO fournisseur (code, raison_sociale, email, telephone, adresse) "
                "VALUES (%s, %s, %s, %s, %s)",
                (code, rs, email, tel, adresse)
            )
            fournisseur_ids.append(curseur.lastrowid)
        print(f"      {len(FOURNISSEURS)} fournisseurs insérés.")

        print("\n  2. Insertion des produits...")
        produit_ids = []
        for ref, desg, prix, stock in PRODUITS:
            curseur.execute(
                "INSERT INTO produit (reference, designation, prix_unitaire, stock) "
                "VALUES (%s, %s, %s, %s)",
                (ref, desg, prix, stock)
            )
            produit_ids.append(curseur.lastrowid)
        print(f"      {len(PRODUITS)} produits insérés.")

        print("\n  3. Insertion des commandes et lignes...")
        for numero, f_idx, statut, lignes in COMMANDES:
            montant_total = sum(PRODUITS[p_idx][2] * qte for p_idx, qte in lignes)
            curseur.execute(
                "INSERT INTO commande (numero, fournisseur_id, montant_total, statut) "
                "VALUES (%s, %s, %s, %s)",
                (numero, fournisseur_ids[f_idx], montant_total, statut)
            )
            commande_id = curseur.lastrowid
            for p_idx, qte in lignes:
                curseur.execute(
                    "INSERT INTO ligne_commande (commande_id, produit_id, quantite, prix_unitaire) "
                    "VALUES (%s, %s, %s, %s)",
                    (commande_id, produit_ids[p_idx], qte, PRODUITS[p_idx][2])
                )
        print(f"      {len(COMMANDES)} commandes insérées avec leurs lignes.")

        connexion.commit()
        print("\n   Données de test insérées avec succès !")

    except Exception as e:
        connexion.rollback()
        print(f"\n   Erreur : {e}")
        raise
    finally:
        db.disconnect()


if __name__ == "__main__":
    print("=" * 60)
    print("  INSERTION DES DONNÉES DE TEST - MySQL")
    print("=" * 60)
inserer_donnees_test()
    print("=" * 60)

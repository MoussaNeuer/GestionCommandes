from daos.fournisseur_dao import FournisseurDAO
from daos.produit_dao import ProduitDAO
from daos.commande_dao import CommandeDAO, LigneCommandeDAO
from models.fournisseur import Fournisseur
from models.produit import Produit
from models.commande import Commande, LigneCommande
import os


class Menu:

    def __init__(self):
        self.fournisseur_dao = FournisseurDAO()
        self.produit_dao = ProduitDAO()
        self.commande_dao = CommandeDAO()
        self.ligne_dao = LigneCommandeDAO()

    def cls(self):
        os.system("clear")

    def pause(self):
        input("Tapez entrer pour continuer ...")

    def menu_principal(self):
        self.cls()
        while True:
            print("=======  MENU PRINCIPAL GESTION COMMANDES  =========")
            print("1. Gestion des fournisseurs")
            print("2. Gestion des produits")
            print("3. Gestion des commandes")
            print("4. Rapports")
            print("5. Quitter")
            print("=====================================================")
            choix = int(input("Faites votre choix : "))
            match choix:
                case 1:
                    self.cls()
                    self.menu_fournisseur()
                case 2:
                    self.cls()
                    self.menu_produit()
                case 3:
                    self.cls()
                    self.menu_commande()
                case 4:
                    self.cls()
                    self.menu_rapport()
                case 5:
                    print("CIAO CIAO et a la prochaine ....")
                    break
                case _:
                    print("--- Choix invalide ---")

    # ===================== FOURNISSEURS =====================

    def menu_fournisseur(self):
        self.cls()
        while True:
            print("======= GESTION DES FOURNISSEURS =========")
            print("1. Afficher tous les fournisseurs")
            print("2. Ajouter un fournisseur")
            print("3. Supprimer un fournisseur")
            print("4. Modifier un fournisseur")
            print("5. Rechercher un fournisseur")
            print("0. Retour")
            choix = int(input("Faites votre choix : "))
            match choix:
                case 1:
                    self.cls()
                    print("============== MES FOURNISSEURS =================")
                    fournisseurs = self.fournisseur_dao.lister_fournisseur()
                    if not fournisseurs:
                        print("Aucun fournisseur disponible dans la base")
                    else:
                        for f in fournisseurs:
                            print(f)
                    self.pause()
                case 2:
                    self.cls()
                    print("============ AJOUTER FOURNISSEUR ==============")
                    fournisseur = Fournisseur()
                    fournisseur.code = input("Entrer le code (ex: F001) : ")
                    fournisseur.raison_sociale = input("Entrer la raison sociale : ")
                    fournisseur.email = input("Entrer l'email : ")
                    fournisseur.telephone = input("Entrer le telephone : ")
                    fournisseur.adresse = input("Entrer l'adresse : ")
                    if self.fournisseur_dao.ajouter_fournisseur(fournisseur):
                        print(f"Fournisseur : {fournisseur.raison_sociale} ajouté avec success")
                    self.pause()
                case 3:
                    id_supprime = int(input("Entrer le ID fournisseur a supprimer : "))
                    # Un fournisseur ne peut pas être supprimé s'il a des commandes
                    nb_commandes = self.fournisseur_dao.compter_commandes(id_supprime)
                    if nb_commandes > 0:
                        print(f"Impossible de supprimer, ce fournisseur a {nb_commandes} commande(s)")
                    else:
                        self.fournisseur_dao.supprimer_fournisseur(id_supprime)
                        print("Fournisseur supprimé avec success")
                    self.pause()
                case 4:
                    id_fournisseur_modifier = int(input("Entrer le ID du fournisseur a modifier : "))
                    fournisseur = self.fournisseur_dao.get_by_id(id_fournisseur_modifier)
                    if fournisseur:
                        fournisseur.code = input("Entrer le nouveau code : ") or fournisseur.code
                        fournisseur.raison_sociale = input("Entrer la nouvelle raison sociale : ") or fournisseur.raison_sociale
                        fournisseur.email = input("Entrer le nouvel email : ") or fournisseur.email
                        fournisseur.telephone = input("Entrer le nouveau telephone : ") or fournisseur.telephone
                        fournisseur.adresse = input("Entrer la nouvelle adresse : ") or fournisseur.adresse
                        self.fournisseur_dao.modifier_fournisseur(fournisseur)
                        print("Fournisseur modifié avec success")
                    else:
                        print("Fournisseur non trouvé")
                    self.pause()
                case 5:
                    mot_cle = input("Entrer le code ou la raison sociale a rechercher : ")
                    fournisseur = self.fournisseur_dao.rechercher_fournisseur(mot_cle)
                    if fournisseur:
                        fournisseur.afficher()
                    else:
                        print("Fournisseur non trouvé")
                    self.pause()
                case 0:
                    self.menu_principal()
                case _:
                    print("--- Choix invalide ---")

    # ===================== PRODUITS =====================

    def menu_produit(self):
        self.cls()
        while True:
            print("======= GESTION DES PRODUITS =========")
            print("1. Afficher tous les produits")
            print("2. Ajouter un produit")
            print("3. Supprimer un produit")
            print("4. Modifier un produit")
            print("5. Rechercher un produit")
            print("6. Alerte stock faible")
            print("0. Retour")
            choix = int(input("Faites votre choix : "))
            match choix:
                case 1:
                    self.cls()
                    print("============== MES PRODUITS =================")
                    produits = self.produit_dao.lister_produit()
                    if not produits:
                        print("Aucun produit disponible dans la base")
                    else:
                        for p in produits:
                            print(p)
                    self.pause()
                case 2:
                    self.cls()
                    print("============ AJOUTER PRODUIT ==============")
                    produit = Produit()
                    produit.reference = input("Entrer la reference (ex: REF001) : ")
                    produit.designation = input("Entrer la designation : ")
                    produit.prix_unitaire = float(input("Entrer le prix unitaire : "))
                    produit.stock = int(input("Entrer le stock : "))
                    if self.produit_dao.ajouter_produit(produit):
                        print(f"Produit : {produit.designation} ajouté avec success")
                    self.pause()
                case 3:
                    id_supprime = int(input("Entrer le ID produit a supprimer : "))
                    # Un produit ne peut pas être supprimé s'il est dans une commande
                    nb_lignes = self.produit_dao.compter_lignes_commande(id_supprime)
                    if nb_lignes > 0:
                        print(f"Impossible de supprimer, ce produit apparait dans {nb_lignes} commande(s)")
                    else:
                        self.produit_dao.supprimer_produit(id_supprime)
                        print("Produit supprimé avec success")
                    self.pause()
                case 4:
                    id_produit_modifier = int(input("Entrer le ID du produit a modifier : "))
                    produit = self.produit_dao.get_by_id(id_produit_modifier)
                    if produit:
                        produit.reference = input("Entrer la nouvelle reference : ") or produit.reference
                        produit.designation = input("Entrer la nouvelle designation : ") or produit.designation
                        prix = input("Entrer le nouveau prix : ")
                        produit.prix_unitaire = float(prix) if prix else produit.prix_unitaire
                        stock = input("Entrer le nouveau stock : ")
                        produit.stock = int(stock) if stock else produit.stock
                        self.produit_dao.modifier_produit(produit)
                        print("Produit modifié avec success")
                    else:
                        print("Produit non trouvé")
                    self.pause()
                case 5:
                    mot_cle = input("Entrer la designation ou la reference a rechercher : ")
                    produit = self.produit_dao.rechercher_produit(mot_cle)
                    if produit:
                        produit.afficher()
                    else:
                        print("Produit non trouvé")
                    self.pause()
                case 6:
                    seuil = int(input("Entrer le seuil de stock : "))
                    produits = self.produit_dao.produits_stock_faible(seuil)
                    if not produits:
                        print(f"Aucun produit avec un stock inferieur a {seuil}")
                    else:
                        for p in produits:
                            print(p)
                    self.pause()
                case 0:
                    self.menu_principal()
                case _:
                    print("--- Choix invalide ---")

    # ===================== COMMANDES =====================

    def menu_commande(self):
        self.cls()
        while True:
            print("======= GESTION DES COMMANDES =========")
            print("1. Afficher toutes les commandes")
            print("2. Creer une commande")
            print("3. Afficher le detail d'une commande")
            print("4. Changer le statut d'une commande")
            print("5. Annuler une commande")
            print("6. Supprimer une commande")
            print("0. Retour")
            choix = int(input("Faites votre choix : "))
            match choix:
                case 1:
                    self.cls()
                    print("============== MES COMMANDES =================")
                    commandes = self.commande_dao.lister_commande()
                    if not commandes:
                        print("Aucune commande disponible dans la base")
                    else:
                        for c in commandes:
                            print(c)
                    self.pause()
                case 2:
                    self.cls()
                    self.creer_commande()
                case 3:
                    id_commande = int(input("Entrer le ID de la commande : "))
                    commande = self.commande_dao.get_by_id(id_commande)
                    if commande:
                        commande.afficher()
                        print("--- Produits de la commande ---")
                        lignes = self.ligne_dao.lister_lignes(id_commande)
                        for ligne in lignes:
                            produit = self.produit_dao.get_by_id(ligne.produit_id)
                            print(f"{produit.designation} x{ligne.quantite} = {ligne.sous_total()} FCFA")
                    else:
                        print("Commande non trouvée")
                    self.pause()
                case 4:
                    self.changer_statut_commande()
                case 5:
                    self.annuler_commande()
                case 6:
                    id_supprime = int(input("Entrer le ID commande a supprimer : "))
                    self.commande_dao.supprimer_commande(id_supprime)
                    print("Commande supprimée avec success")
                    self.pause()
                case 0:
                    self.menu_principal()
                case _:
                    print("--- Choix invalide ---")

    def creer_commande(self):
        print("============ CREER COMMANDE ==============")
        commande = Commande()
        commande.numero = input("Entrer le numero de commande (ex: CMD001) : ")

        print("--- Fournisseurs disponibles ---")
        fournisseurs = self.fournisseur_dao.lister_fournisseur()
        for f in fournisseurs:
            print(f)
        commande.fournisseur_id = int(input("Entrer le ID du fournisseur : "))
        commande.montant_total = 0
        commande.statut = "EN_ATTENTE"

        self.commande_dao.ajouter_commande(commande)
        id_commande = self.commande_dao.get_dernier_id()

        montant_total = 0
        while True:
            print("--- Produits disponibles ---")
            produits = self.produit_dao.lister_produit()
            for p in produits:
                print(p)
            ajout = input("Voulez vous ajouter un produit ? (oui/non) : ")
            if ajout != "oui":
                break
            id_produit = int(input("Entrer le ID du produit : "))
            quantite = int(input("Entrer la quantite : "))

            produit = self.produit_dao.get_by_id(id_produit)
            if not produit:
                print("Produit non trouvé")
                continue
            if quantite > produit.stock:
                print(f"Stock insuffisant, stock disponible : {produit.stock}")
                continue

            ligne = LigneCommande()
            ligne.commande_id = id_commande
            ligne.produit_id = id_produit
            ligne.quantite = quantite
            ligne.prix_unitaire = produit.prix_unitaire
            self.ligne_dao.ajouter_ligne(ligne)

            montant_total = montant_total + (quantite * produit.prix_unitaire)
            print(f"Produit {produit.designation} ajouté à la commande")

        self.commande_dao.modifier_montant(id_commande, montant_total)
        print(f"Commande {commande.numero} créée avec success, montant total : {montant_total} FCFA")
        self.pause()

    def changer_statut_commande(self):
        # Ordre des statuts : le statut ne peut pas reculer
        ordre_statuts = ["EN_ATTENTE", "VALIDEE", "LIVREE"]

        id_commande = int(input("Entrer le ID de la commande : "))
        commande = self.commande_dao.get_by_id(id_commande)
        if not commande:
            print("Commande non trouvée")
            self.pause()
            return

        print(f"Statut actuel : {commande.statut}")
        print("1. VALIDEE")
        print("2. LIVREE")
        choix = int(input("Nouveau statut : "))

        match choix:
            case 1:
                nouveau_statut = "VALIDEE"
            case 2:
                nouveau_statut = "LIVREE"
            case _:
                print("Choix invalide")
                self.pause()
                return

        # Vérifier que le statut ne recule pas
        if ordre_statuts.index(nouveau_statut) <= ordre_statuts.index(commande.statut):
            print("Impossible, le statut ne peut pas reculer")
            self.pause()
            return

        # Si on passe a VALIDEE, on deduit le stock des produits
        if nouveau_statut == "VALIDEE":
            lignes = self.ligne_dao.lister_lignes(id_commande)
            for ligne in lignes:
                produit = self.produit_dao.get_by_id(ligne.produit_id)
                if ligne.quantite > produit.stock:
                    print(f"Stock insuffisant pour {produit.designation}")
                    self.pause()
                    return
            for ligne in lignes:
                produit = self.produit_dao.get_by_id(ligne.produit_id)
                nouveau_stock = produit.stock - ligne.quantite
                self.produit_dao.mettre_a_jour_stock(produit.id, nouveau_stock)

        self.commande_dao.modifier_statut(id_commande, nouveau_statut)
        print(f"Statut changé en {nouveau_statut} avec success")
        self.pause()

    def annuler_commande(self):
        id_commande = int(input("Entrer le ID de la commande a annuler : "))
        commande = self.commande_dao.get_by_id(id_commande)
        if not commande:
            print("Commande non trouvée")
            self.pause()
            return
        if commande.statut == "LIVREE":
            print("Impossible d'annuler une commande deja livree")
            self.pause()
            return

        # Si la commande etait validee, on remet le stock
        if commande.statut == "VALIDEE":
            lignes = self.ligne_dao.lister_lignes(id_commande)
            for ligne in lignes:
                produit = self.produit_dao.get_by_id(ligne.produit_id)
                nouveau_stock = produit.stock + ligne.quantite
                self.produit_dao.mettre_a_jour_stock(produit.id, nouveau_stock)

        self.commande_dao.modifier_statut(id_commande, "ANNULEE")
        print("Commande annulée avec success")
        self.pause()

    # ===================== RAPPORTS =====================

    def menu_rapport(self):
        self.cls()
        while True:
            print("======= RAPPORTS =========")
            print("1. Commandes par fournisseur")
            print("2. Commandes en attente")
            print("3. Valeur totale du stock")
            print("4. Top 5 produits les plus commandés")
            print("5. Chiffre d'affaires total")
            print("0. Retour")
            choix = int(input("Faites votre choix : "))
            match choix:
                case 1:
                    id_fournisseur = int(input("Entrer le ID du fournisseur : "))
                    commandes = self.commande_dao.commandes_du_fournisseur(id_fournisseur)
                    if not commandes:
                        print("Aucune commande pour ce fournisseur")
                    else:
                        for c in commandes:
                            print(c)
                    self.pause()
                case 2:
                    commandes = self.commande_dao.commandes_en_attente()
                    if not commandes:
                        print("Aucune commande en attente")
                    else:
                        for c in commandes:
                            print(c)
                    self.pause()
                case 3:
                    produits = self.produit_dao.lister_produit()
                    valeur_totale = 0
                    for p in produits:
                        valeur_totale = valeur_totale + (p.prix_unitaire * p.stock)
                    print(f"Valeur totale du stock : {valeur_totale} FCFA")
                    self.pause()
                case 4:
                    resultats = self.ligne_dao.top5_produits()
                    if not resultats:
                        print("Aucune donnée disponible")
                    else:
                        for produit_id, total_quantite in resultats:
                            produit = self.produit_dao.get_by_id(produit_id)
                            print(f"{produit.designation} : {total_quantite} unités commandées")
                    self.pause()
                case 5:
                    ca = self.commande_dao.chiffre_affaires()
                    print(f"Chiffre d'affaires total : {ca} FCFA")
                    self.pause()
                case 0:
                    self.menu_principal()
                case _:
                    print("--- Choix invalide ---")

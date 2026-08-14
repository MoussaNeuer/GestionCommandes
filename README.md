# Gestion des Commandes Fournisseurs

Projet de Programmation - POO & Base de données  
Classe : Licence 2 - Informatique de Gestion (IAGE)  
Enseignant : M. DIALLO

---

## Description

Application console en Python (POO) avec une base de données MySQL permettant de gérer les fournisseurs, les produits et les commandes d'une entreprise de distribution de matériel informatique.

---

## Prérequis

- Python 3.10+
- MySQL Server
- mysql-connector-python

---

## Installation

1. Cloner le dépôt :
```
git clone https://github.com/MoussaNeuer/gestion-commandes.git
cd gestion-commandes
```

2. Installer les dépendances :
```
pip install -r requirements.txt
```

3. Créer la base de données dans MySQL :
```sql
CREATE DATABASE gestion_commandes_iage CHARACTER SET utf8mb4;
```
---

## Structure du projet

```
gestion_commandes/
│
├── database/
│   ├── config.py        # Configuration BD
│   └── connexion.py     # Singleton de connexion
│
├── models/
│   ├── fournisseur.py   # Classe Fournisseur
│   ├── produit.py       # Classe Produit
│   └── commande.py      # Classes Commande et LigneCommande
│
├── daos/
│   ├── fournisseur_dao.py  # CRUD Fournisseur
│   ├── produit_dao.py      # CRUD Produit
│   └── commande_dao.py     # CRUD Commande + lignes + rapports
│
├── menu/
│   └── interface.py     # Interface utilisateur console
│
├── create_tables.py     # Création des tables SQL
├── insert_test_data.py  # Données de test
├── main.py              # Point d'entrée
└── requirements.txt
```

---

## Fonctionnalités

- **Fournisseurs** : Ajouter, lister, rechercher, modifier, supprimer
- **Produits** : Ajouter, lister, rechercher, modifier, supprimer, alerte stock
- **Commandes** : Créer, lister, détail, changer statut, annuler, supprimer
- **Rapports** : Commandes par fournisseur, commandes en attente, valeur du stock, top 5 produits, chiffre d'affaires

## Membres du Groupe
- **Moussa LO
- **Djiby NDIAYE
- **Hadya DIAGANA
- **Maty GNINGUE

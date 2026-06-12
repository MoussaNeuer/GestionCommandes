import mysql.connector
from database.config import TYPE_BD, MYSQL

class DatabaseConnection:
    # singleton pour la cconnexion à la base de données
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = None
            cls._instance.cursor = None
        return cls._instance

    def connect(self):
        # connexion à la base de données
        try:
            if TYPE_BD == "mysql":
                self.connection = mysql.connector.connect(
                    host=MYSQL["host"],
                    port=MYSQL["port"],
                    user=MYSQL["user"],
                    password=MYSQL["password"],
                    database=MYSQL["database"]
                )
                self.cursor = self.connection.cursor()
                print("Connexion à la base de données MySQL réussie.")
                return True
            else:
                print(f"Type de base de données '{TYPE_BD}' non supporté.")
                return False
        except Exception as e:
            print(f"Erreur de connexion à la base de données: {e}")
            return False  

    def disconnect(self):
        # déconnexion de la base de données
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Déconnexion de la base de données réussie.")

    def commit(self):
        # valider les changements dans la base de données
        if self.connection:
            self.connection.commit()

    def rollback(self):
        # annuler les changements dans la base de données
        if self.connection:
            self.connection.rollback()

    def execute(self, query, params=None):
        # exécuter une requête SQL
            try:
                self.cursor.execute(query, params)
                return True
            except Exception as e:
                print(f"Erreur lors de l'exécution de la requête: {e}")
                return False

    def fetchall(self):
        # récupérer tous les résultats d'une requête
        if self.cursor:
            return self.cursor.fetchall()
        return None

    def fetchone(self):
        # récupérer un seul résultat d'une requête
        if self.cursor:
            return self.cursor.fetchone() 
        return None       
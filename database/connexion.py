import mysql.connector
from database.config import MYSQL


class DatabaseConnection:
    # Singleton : une seule instance de connexion
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = None
            cls._instance.cursor = None
        return cls._instance

    def connect(self):
        """Établir la connexion à la base de données MySQL"""
        try:
            self.connection = mysql.connector.connect(
                host=MYSQL["host"],
                port=MYSQL["port"],
                database=MYSQL["database"],
                user=MYSQL["user"],
                password=MYSQL["password"]
            )
            self.cursor = self.connection.cursor()
            return True
        except Exception as e:
            print(f"Erreur de connexion : {e}")
            return False

    def disconnect(self):
        """Fermer la connexion"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def commit(self):
        """Valider la transaction"""
        if self.connection:
            self.connection.commit()

    def rollback(self):
        """Annuler la transaction"""
        if self.connection:
            self.connection.rollback()

    def execute(self, query, params=None):
        """Exécuter une requête SQL paramétrée"""
        try:
            self.cursor.execute(query, params or ())
            return True
        except Exception as e:
            print(f"Erreur SQL : {e}")
            raise

    def fetchall(self):
        """Récupérer tous les résultats"""
        return self.cursor.fetchall()

    def fetchone(self):
        """Récupérer un seul résultat"""
        return self.cursor.fetchone()

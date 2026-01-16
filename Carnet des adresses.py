import sys
import sqlite3
from abc import ABC, abstractmethod

from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QGridLayout, QFrame,
    QLineEdit, QLabel, QTableWidget, QTableWidgetItem

class BaseDatabase(ABC):
    @abstractmethod
    def creer_table(self):
        pass
    @abstractmethod
    def inserer_personne(self, pid, nom, prenom, mail):
        pass
    @abstractmethod
    def modifier_personne(self, pid, nom, prenom, mail):
        pass
    @abstractmethod
    def supprimer_personne(self, pid):
        pass
    @abstractmethod
    def selectionner_tout(self):
        pass

class SQLitePersonsDatabase(BaseDatabase):

    def __init__(self, db_name="carnet_adresse.db"):
        self.db_name = db_name

    def _connexion(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        return conn, cursor

    def creer_table(self):
        conn, cursor = self._connexion()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS Persons("
            "PersonID int, "
            "Nom varchar(255), "
            "Prenom varchar(255), "
            "Mail varchar(255)"
            ");"
        )
        conn.commit()
        conn.close()

    def inserer_personne(self, pid, nom, prenom, mail):
        conn, cursor = self._connexion()
        requete = (
            "INSERT INTO Persons VALUES ("
            + str(pid) + ",'"
            + nom + "','"
            + prenom + "','"
            + mail + "');"
        )
        cursor.execute(requete)
        conn.commit()
        conn.close()

    def modifier_personne(self, pid, nom, prenom, mail):
        conn, cursor = self._connexion()
        requete = (
            "UPDATE Persons SET "
            "Nom='" + nom + "', "
            "Prenom='" + prenom + "', "
            "Mail='" + mail + "' "
            "WHERE PersonID=" + str(pid) + ";"
        )
        cursor.execute(requete)
        conn.commit()
        conn.close()

    def supprimer_personne(self, pid):
        conn, cursor = self._connexion()
        requete = "DELETE FROM Persons WHERE PersonID=" + str(pid) + ";"
        cursor.execute(requete)
        conn.commit()
        conn.close()

    def selectionner_tout(self):
        conn, cursor = self._connexion()
        cursor.execute("SELECT * FROM Persons")
        resultat = cursor.fetchall()
        conn.close()
        return resultat

class Annuaire:

    def __init__(self, db: BaseDatabase):
        self.db = db

    def creer_table(self):
        self.db.creer_table()

    def ajouter(self, pid, nom, prenom, mail):
        self.db.inserer_personne(pid, nom, prenom, mail)

    def modifier(self, pid, nom, prenom, mail):
        self.db.modifier_personne(pid, nom, prenom, mail)

    def supprimer(self, pid):
        self.db.supprimer_personne(pid)

    def tout(self):
        return self.db.selectionner_tout()
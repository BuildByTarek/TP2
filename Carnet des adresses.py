import sys
import sqlite3
from abc import ABC, abstractmethod

from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QGridLayout, QFrame,
    QLineEdit, QLabel, QTableWidget, QTableWidgetItem)

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

base = SQLitePersonsDatabase("carnet.db")
annuaire = Annuaire(base)

def creer_table():
    annuaire.creer_table()
    afficher_tout()

def inserer():
    pid = qLineID.text()
    nom = qLineNom.text()
    prenom = qLinePrenom.text()
    mail = qLineMail.text()
    annuaire.ajouter(pid, nom, prenom, mail)
    afficher_tout()

def enregistrer_modification():
    pid = qLineID.text()
    nom = qLineNom.text()
    prenom = qLinePrenom.text()
    mail = qLineMail.text()
    annuaire.modifier(pid, nom, prenom, mail)
    afficher_tout()

def supprimer():
    pid = qLineSuppID.text()
    annuaire.supprimer(pid)
    afficher_tout()

def afficher_tout():
    resultat = annuaire.tout()

    qtab.setRowCount(len(resultat))
    qtab.setColumnCount(4)
    qtab.setHorizontalHeaderLabels(["id", "nom", "prenom", "mail"])

    for i in range(len(resultat)):
        for j in range(4):
            qtab.setItem(i, j, QTableWidgetItem(str(resultat[i][j])))

def get_clicked_cell(row, column):
    id_item = qtab.item(row, 0)
    nom_item = qtab.item(row, 1)
    prenom_item = qtab.item(row, 2)
    mail_item = qtab.item(row, 3)

    if id_item:
        qLineID.setText(id_item.text())
        qLineSuppID.setText(id_item.text())

    if nom_item:
        qLineNom.setText(nom_item.text())

    if prenom_item:
        qLinePrenom.setText(prenom_item.text())

    if mail_item:
        qLineMail.setText(mail_item.text())
app = QApplication(sys.argv)
win = QWidget()
win.setGeometry(100, 100, 700, 500)
win.setWindowTitle("Carnet d'adresses")

frame = QFrame(win)
frame.setGeometry(20, 20, 660, 460)

grid = QGridLayout()
frame.setLayout(grid)
labelTitre = QLabel(win)
labelTitre.setText("Carnet d'adresses")
grid.addWidget(labelTitre, 0, 0, 1, 4)
labelID = QLabel(win)
labelID.setText("ID")
grid.addWidget(labelID, 1, 0)

labelNom = QLabel(win)
labelNom.setText("Nom")
grid.addWidget(labelNom, 1, 1)

labelPrenom = QLabel(win)
labelPrenom.setText("Prénom")
grid.addWidget(labelPrenom, 1, 2)

labelMail = QLabel(win)
labelMail.setText("E-Mail")
grid.addWidget(labelMail, 1, 3)

qLineID = QLineEdit(win)
grid.addWidget(qLineID, 2, 0)

qLineNom = QLineEdit(win)
grid.addWidget(qLineNom, 2, 1)

qLinePrenom = QLineEdit(win)
grid.addWidget(qLinePrenom, 2, 2)

qLineMail = QLineEdit(win)
grid.addWidget(qLineMail, 2, 3)


labelSupp = QLabel(win)
labelSupp.setText("ID à supprimer")
grid.addWidget(labelSupp, 3, 0)

qLineSuppID = QLineEdit(win)
grid.addWidget(qLineSuppID, 3, 1)


btnCreer = QPushButton(win)
btnCreer.setText("Créer Table")
btnCreer.clicked.connect(creer_table)
grid.addWidget(btnCreer, 4, 0)

btnInserer = QPushButton(win)
btnInserer.setText("Insérer")
btnInserer.clicked.connect(inserer)
grid.addWidget(btnInserer, 4, 1)

btnModifier = QPushButton(win)
btnModifier.setText("Modifier-Enregistrer")
btnModifier.clicked.connect(enregistrer_modification)
grid.addWidget(btnModifier, 4, 2)

btnSupprimer = QPushButton(win)
btnSupprimer.setText("DELETE")
btnSupprimer.clicked.connect(supprimer)
grid.addWidget(btnSupprimer, 4, 3)

btnAfficher = QPushButton(win)
btnAfficher.setText("Afficher Tout")
btnAfficher.clicked.connect(afficher_tout)
grid.addWidget(btnAfficher, 5, 0)

qtab = QTableWidget(win)
qtab.setRowCount(4)
qtab.setColumnCount(4)
qtab.setHorizontalHeaderLabels(["ID", "nom", "prenom", "mail"])
qtab.cellClicked.connect(get_clicked_cell)
grid.addWidget(qtab, 6, 0, 2, 4)

win.show()
sys.exit(app.exec())
import sys
import sqlite3
from abc import ABC, abstractmethod

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

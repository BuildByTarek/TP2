# TP2 : P.O.O
Carnet d'Adresses
Description
C'est une application pour gérer un carnet d’adresses. Tu peux ajouter, modifier, supprimer et afficher des personnes avec leur ID, nom, prénom et email.
L'app utilise SQLite pour la base de données et PyQt6 pour l'interface graphique. C'est une application simple pour  gérer des contacts.
Fonctionnalités
•	Créer Table - Crée la table dans la base de données
•	Insérer - Ajoute une nouvelle personne (ID, Nom, Prénom, Email)
•	Modifier-Enregistrer - Change les infos d'une personne existante
•	DELETE - Supprime une personne par son ID
•	Afficher Tout - Montre toutes les personnes dans le tableau
•	Cliquer sur une ligne - Remplit automatiquement les champs avec les données
Comment l'utiliser
1.	Créer la table d'abord - Clique sur "Créer Table" pour initialiser la base de données
2.	Ajouter une personne - Remplis les champs (ID, Nom, Prénom, Email) et clique "Insérer"
3.	Voir les données - Clique "Afficher Tout" pour voir tout le monde dans la table
4.	Modifier - Clique sur une ligne, change ce que tu veux, puis clique "Modifier-Enregistrer"
5.	Supprimer - Entre l'ID à supprimer et clique "DELETE"
Architecture
Classes
BaseDatabase - Interface abstraite (ABC) qui définit les méthodes principales
SQLitePersonsDatabase - Implémente BaseDatabase avec SQLite
•	creer_table() - Crée la table Persons
•	inserer_personne() - Ajoute une personne
•	modifier_personne() - Modifie une personne
•	supprimer_personne() - Supprime une personne
•	selectionner_tout() - Retourne toutes les personnes
Annuaire : Fait le lien entre l'interface et la base de données
Interface PyQt6
L'app a une grille avec :
•	Des champs de texte (QLineEdit) pour entrer les données
•	Des boutons (QPushButton) pour les actions
•	Un tableau (QTableWidget) pour afficher les données
Prérequis
Python 
PyQt6
sqlite3 (inclus dans Python)

Notes
•	La base de données se crée automatiquement (carnet.db)
•	Les données sont sauvegardées dans SQLite
Améliorations possibles
•	Ajouter un ID auto-généré
•	Meilleure gestion des erreurs
•	Chercher des personnes par nom

#importation de "sqlite3"
import sqlite3
#etablir la connection vers la base "sqlite3"
#la base de donné s'appelle "ma_base" .db extension
cnx = sqlite3.Connection('ma_base.db')
#creation d'un cursor pour créer la table "user". Cette table contiendra la liste de tout les pseudos avec la liste de mots de passes
createur_table = cnx.cursor()
#execution de "cursor" avec la commande sql en parametre
createur_table.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     login TEXT,
     mdp text
)
""")
#validation de la commande de création de table
cnx.commit()
#fermeture de la connection
cnx.close()
#IMPORTANT: NE JAMIAIS OUBLIER DE FERMER LA CONNECTION
# importation de "sql_db"
import sql_db
#
cnx2 = sql_db.sqlite3.Connection('database.db')
createur_ligne = cnx2.cursor()

CreateUser = input("Veuillez créer votre pseudo:")
CreatePassword = input("Veuillez saisir un nouveau mot de passe:")

data = {"login" : CreateUser, "mdp" : CreatePassword}

createur_ligne.execute("""
INSERT INTO users(login, mdp) VALUES(:login, :mdp)""", data)
cnx2.commit()
cnx2.close()

#confirmation de fin de création de login et mot e passe
print("Votre compte a bien été crée :)")

# Demande de login
User = input("Pseudo:")

if User != CreateUser:
    while User != CreateUser:
        User = input("votre pseudo n'est pas valide, veuillez resaisir votre pseudo: ")

# Login correct, passons à la demande de mot de passe...
Password = input("Veuillez saisir votre mot de passe:")

#Demande mot de passe tant que le mot de passe n'est pas bon...
while Password != CreatePassword:
    Password = input("votre mot de passe n'est pas valide, veuillez resaisir votre mot de passe:")

# Login et mot de passe correct, message de bienvenue...
print("Bienvenu " + User)
    

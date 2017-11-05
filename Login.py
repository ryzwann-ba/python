CreateUser = input("Veuillez créer votre pseudo:")
CreatePassword = input("Veuillez saisir un nouveau mot de passe:")

#confirmation de fin de création de login et mot e passe
print("Votre compte a bien été crée :)")

# Demande de login
User = input("Pseudo:")

if User != CreateUser:
    while User != CreateUser:
        print("The Username is not correct, please check this...")
        User = input("Try again username:")

# Login correct, passons à la demande de mot de passe...
Password = input("password:")

#Demande mot de passe tant que le mot de passe n'est pas bon...
while Password != CreatePassword:
    print("The password is not correct, please check this...")
    Password = input("Try again password:")

# Login et mot de passe correct, message de bienvenue...
print("Welcome " + User)
    

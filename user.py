import login

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

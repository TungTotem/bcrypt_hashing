import bcrypt

# password = input("Gib dein Passwort ein")
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(input("gib dein password ein").encode("utf-8"), salt)


print(hashed_password)

if bcrypt.checkpw(input("gib dein ursprüngliches passwort ein").encode('utf-8'), hashed_password):
    print("passwort ist korrekt")
else:
    print("PW ist falsch")

    

def check_login(names_and_passwords):
    username = input("Benutzername: ")
    password = input("Passwort: ")

    if password == names_and_passwords[username]:
        return True

    else:
        return False

def add_user(names_and_passwords):
    username = input("Bitte geben Sie den neuen Benutzernamen ein: ")

    usernames = names_and_passwords.keys()

    if username in usernames:
        print("Der Benutzername ist bereits vergeben. Bitte wählen Sie einen anderen Benutzernamen")

        return False

    else:
        password = input("Bitte geben Sie ein neues Passwort ein: ")
        names_and_passwords[username] = password

def remove_user(user_and_passwords):
    username = input("Bitte geben Sie den Benutzernamen welchen Sie entfernen wollen ein: ")

    if username in user_and_passwords:
        safety = input("Wollen sie den Benutzer " + username + " wirklich entfernen? (J/N): ")

        if safety == "J" or safety == "j":
            user_and_passwords.pop(username)
            print("Der Benutzer " + username + " wurde entfernt.")

        else:
            print("Der Benutzer wurde nicht entfernt.")

    else:
        print("Der Benutzer ist nicht vorhanden.")


dictionary = {"hans": "abcd",
              "peter": "abcd",
              "root": "ASKakdfh23423Ajd"}

remove_user(dictionary)

'''
while True:
    if check_login(dictionary):
        print("Login erfolgreich!")
        break
'''



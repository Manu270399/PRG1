from datetime import datetime

def addUserToList(listOfUserObjects):
    userObject = dict() # {}

    userObject["username"] = input("Bitte geben Sie einen Benutzernamen ein: ")
    userObject["password"] = input("Bitte geben Sie eine Passwort ein: ")
    userObject["valid"] = True
    userObject["passwordChanged"] = datetime.now()
    userObject["e-mail"] = "lord@kelvin.org"

    listOfUserObjects.append(userObject)

def checkYear(listOfUserObjects):
    for userObjects in listOfUserObjects:
        if userObjects["passwordChanged"] < datetime(2022,1,1 ):
            userObjects["valid"] = False

def Valid(listOfUserObjects):
    for userObjects in listOfUserObjects:
        if userObjects["valid"] == False:
            userObjects["password"] = input("Bitte geben Sie ein neues Passwort für den Benutzer " + userObjects["username"] + " ein: ")
            userObjects["valid"] = True

def checkMailAdresses(listOfUserObjects):
    for i, userObjects in enumerate(listOfUserObjects):
        for j in range(i + 1, len(listOfUserObjects)):
            if userObjects["e-mail"] == listOfUserObjects[j]["e-mail"]:
                print("Die Mail " + userObjects["e-mail"] + " gibt es schon.")



    # Aufgabe 1: Welche Aufgabe implementiert die Funktion addUserToList?

    # Aufgabe 2: Ändern Sie die Funktion so ab, dass der Anwender bei jedem Aufruf den Benutzernamen
    # und das Passwort über die Konsole eingeben muss.

    # Aufgabe 3: Ändern Sie das Änderungsdatum des Passworts auf die aktuelle Uhrzeit.

# Aufgabe 4:
#
# Erstellen Sie eine Funktion checkYear mit dem Parameter listOfUserObjects. Der Parameter
# beinhaltet eine Liste mit allen Benutzerobjekten.

# Aufgabe 5:
#
# Implementieren Sie nun die Funktion für die Aufgabe 4. Alle Benutzer seit dem
# Jahr 2022 ihr Kennwort nicht geändert haben, werden deaktiviert, in dem der Key valid
# den Value False erhält.

# Aufgabe 6:
#
# Erstellen Sie eine Funktion setValid mit dem Parameter listOfUserObjects. Der Parameter
# beinhaltet eine Liste mit allen Benutzerobjekten.
#
# Gehen Sie alle Benutzer der Liste des Parameter durch. Jeder Benutzer, welcher
# deaktivert wurde (siehe Aufgabe 5) erhält ein neues Passwort. Das Passwort gibt der
# Anwender über einen input ein. Zudem wird der Value für den valid-Key auf True gesetzt.

# Aufgabe 7:
#
# Prüfen Sie, mittels der Funktion checkMailAdresses(), ob doppelte E-Mail-Adressen vorliegen.

# In dem folgenden Bereich nehmen Sie keine Änderungen vor!
# Testdaten:
userList = list()

user = dict()
user["username"] = "peter.meyer"
user["password"] = "wer2"
user["valid"] = True
user["passwordChanged"] = datetime(2021, 2, 21)
user["e-mail"] = "peter@web.de"

userList.append(user)

user = dict()
user["username"] = "franz.huber"
user["password"] = "Passwort"
user["valid"] = False
user["passwordChanged"] = datetime(2023, 3, 1)
user["e-mail"] = "hubi@gmx.de"

userList.append(user)

user = dict()
user["username"] = "julia.meyer"
user["password"] = "abc123"
user["valid"] = True
user["passwordChanged"] = datetime(2024, 1, 2)
user["e-mail"] = "jule@meyer.de"

userList.append(user)


# Ab hier können Sie Ihre Lösungen testen:
addUserToList(userList)
checkYear(userList)
Valid(userList)
checkMailAdresses(userList)
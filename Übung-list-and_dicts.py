from datetime import datetime

def setDatetime():
    year = int(input("Geburtsjahr: "))
    month = int(input("Monat: "))
    day = int(input("Tag: "))

    return datetime(year, month, day)

def addUserToList (listOfUserObjects):
    userObject = {} #dict()

    userObject["prename"] = input("Vorname: ")
    userObject["lastname"] = input("Nachname: ")
    userObject["e-mail"] = "lord@kelvin.org"
    userObject["password"] = "SehrSicher"
    userObject["valid"] = True
    userObject["birthday"] = setDatetime()

    listOfUserObjects.append(userObject)

def printUserObject(userObject):

    print("Vorname:", userObject["prename"])
    print("Nachname:", userObject["lastname"])
    print("E-Mail:", userObject["e-mail"])
    print("Passwort:", userObject["password"])

    date = userObject["birthday"]
    date_as_string = str(date.year) + "-" +  str(date.month) + "-" + str(date.day)
    print("Geburtstag:", date_as_string)


def checkValidUsers(listOfUserObjects):

    validUsers = list()

    for userObject in listOfUserObjects:
        if userObject["valid"] == True:
            validUsers.append(userObject["lastname"] + ", " + userObject["prename"])

    return validUsers

def changePassword(listOfUserObjects):

    username = input("Bitte geben Sie einen Benutzernamen (e-mail) ein: ")
    user = None

    for userObject in listOfUserObjects:
        if userObject["e-mail"] == username:
            user = userObject

            break

    if user == None:
        print("Unbekannter Benutzer")

        return

    user["password"] = input("Bitte geben Sie ein neues Passwort ein: ")

    for userObject in listOfUserObjects:
        if userObject["password"] == user["password"] and userObject["e-mail"] != user["e-mail"]:
           print("passwort ist bereits vergeben")

           while userObject["password"] == user["password"]:
                user["password"] = input("Bitte geben Sie ein neues Passwort ein: ")


list_of_userobjects = [] #list()


#Beispiel Daten
userObject = {}  # dict()

userObject["prename"] = "Fabian"
userObject["lastname"] = "Rödel"
userObject["e-mail"] = "Fabi.Rödel@gmail.com"
userObject["password"] = "dskhflasd"
userObject["valid"] = True
userObject["birthday"] = datetime(2000, 8, 31)

list_of_userobjects.append(userObject)


addUserToList(list_of_userobjects)
printUserObject(list_of_userobjects[0])
changePassword(list_of_userobjects[0])



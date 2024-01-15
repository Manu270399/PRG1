
def check_username_and_password(usernames, passwords):
    username = input("Benutzername: ")
    password = input("Passwort: ")

    length = len(usernames)
    counter = 0

    while counter < length:
        if username == usernames[counter]:
            if password == passwords[counter]:
                return True

        counter += 1

    return False

usernames_list = ["hans", "hans", "peter"]
passwords_list = ["abc", "123", "dskajlh123AFrsdE"]

while True:
    if check_username_and_password(usernames_list, passwords_list):
        print("Login erfolgreich!")
        break



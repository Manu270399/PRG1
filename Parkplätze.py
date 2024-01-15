from datetime import datetime

### Parking spaces and time in list ###
parking_space = [""] * 6
parking_time = [None] * 6

### saving number plate for parking lot ###
def set_parkingspace():
    parking_lot = int(input("Bitte geben Sie Ihre Parkplatznummer ein (1-6): "))

    if parking_lot < 1 or parking_lot > 6:
        print("Ungültige Parkplatznummer. Bitte wählen Sie eine Nummer zwischen 1 und 6.")
        return

    if parking_space[parking_lot - 1] == "":
        number_plate = input("Geben Sie Ihr Kennzeichen ein: ")
        parking_space[parking_lot - 1] = number_plate
        parking_time[parking_lot - 1] = datetime.now()
        print("Parkplatz", parking_lot, "wurde erfolgreich belegt.")

    else:
        print("Parkplatz", parking_lot, "wurde bereits belegt.")

### setting free parking lots ###
def free_parkingspace():
    choice = int(input("Bitte wählen Sie ob Sie Ihren Parkplatz (1) oder Ihr Kennzeichen (2) eingeben wollen: "))
    if choice < 1 or choice > 2:
        print("Ungültige Eingabe. Bitte geben Sie 1 oder 2 ein.")


    if choice == 1:
        parking_lot = int(input("Bitte geben Sie Ihre Parkplatznummer ein (1-6): "))

        if parking_lot < 1 or parking_lot > 6:
            print("Ungültige Parkplatznummer. Bitte wählen Sie eine Nummer zwischen 1 und 6.")
            return

        if parking_space[parking_lot - 1] != "":
            parking_space[parking_lot - 1] = ""
            print("Parkplatz", parking_lot, "wurde erfolgreich frei gegeben.")

        else:
            print("Der Parkplatz ist bereits leer.")
            return

    if choice == 2:
        number_plate = input("Bitte geben Sie Ihr Kennzeichen ein: ")

        if number_plate in parking_space:
            number_plate = parking_space.index(number_plate)
            parking_lot = number_plate + 1
            parking_space[number_plate] = ""
            print("Parkplatz", parking_lot, "wurde erfolgreich frei gegeben.")

        else:
            print("Kennzeichen nicht gefunden. Bitte überprüfen Sie Ihre Eingabe.")
            return

set_parkingspace()
free_parkingspace()









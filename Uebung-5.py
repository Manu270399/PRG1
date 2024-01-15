'''
run = True

while run == True:
    gender = input("Bitte geben Sie Ihr Geschlecht (m/w/d) ein: ")

    if gender == "m" or gender == "w" or gender == "d":
        break
    else:
        print("Eingabe unzulässig.")

print("Sie haben als Geschlecht", gender, "gewählt.")
'''

'''
while True:
    digit = float(input("Bitte geben Sie eine Zahl zwischen 0 und 100 ein: "))
    if digit < 100 and digit > 0:
        print(digit)
        break
    elif digit < 0:
            print("Zu klein!")
    elif digit > 100:
            print("Zu groß!")
'''
'''
from random import *
mystery_number = int(randint(1, 100))
while True:
    number = float(input("Bitte geben Sie eine Zahl zwischen 0 und 100 ein: "))
    if number < 100 and number > 0:
        if number < mystery_number:
            print("Ihre Zahl ist zu klein!")
        elif number > mystery_number:
            print("Ihre Zahl ist zu groß!")
        elif number == mystery_number:
            print("Herzlichen Glückwunsch!")
            break
    elif number <= 0:
        print("Ihre Zahl liegt unter dem gewünschten Bereich!")
    elif number >= 100:
        print("Ihre Zahl liegt über dem gewünschten Bereich!")
'''
'''
time_limit = 560
while True:
    worktime = int(input("Bitte geben Sie Ihre Arbeitszeit (min) ein: "))
    kind_of_work = input("Bitte geben Sie Ihre Tätigkeit ein: ")
    print(kind_of_work, "(" + str(worktime) + " min)")
    whole_worktime = 0
    if worktime <= time_limit:
        worktime_2 = int(input("Bitte geben Sie Ihre Arbeitszeit (min) ein: "))
        kind_of_work_2 = input("Bitte geben Sie Ihre Tätigkeit ein: ")
        print(kind_of_work_2, "(" + str(worktime_2) + " min)")
        whole_worktime = worktime + worktime_2
        worktime = whole_worktime
        if whole_worktime > time_limit:
            print("Feierabend!")
            overtime = whole_worktime - time_limit
            print("Sie haben " + str(overtime) + " min zu viel gearbeitet.")
            break
    elif worktime > time_limit:
        print("Feierabend!")
        print("Sie haben" + str(worktime - time_limit) + "min zu viel gearbeitet.")
        break
'''
'''
work_time_per_week = 0
days = 0
while days < 5:
    days += 1
    working_time = 0

    while working_time < 560:
        task = input("Welche Aufgabe wurde bearbeitet? ")
        task_time = int(input("Wie lange haben Sie für die Aufgabe benötigt? "))

    #   working_time = working_time + task_time
        working_time += task_time

    print("Feierabend!")

    extra_time = working_time - 560

    print("Sie haben heute", extra_time, "Minuten mehr gearbeitet.")

    work_time_per_week += extra_time
print("Wochenende!")
print("Sie haben diese Woche", work_time_per_week, "Minuten mehr gearbeitet.")
'''

counter_class = 0
counter_all_students = 0
counter_student = 0
terminator = "---"
list_of_students = list()

while True:
    class_name = input("Bitte geben Sie den Klassennamen ein: ")

    if class_name == terminator:
        print("Eingabe beendet")
        break

    else:
        print("Sie haben die Klasse", class_name, "gewählt.")
        counter_class += 1
        print("Sie haben", counter_class, "Klassen erstellt.")

    while True:
        student_name = input("Bitte geben Sie den Name des Schülers ein: ")

        if student_name == terminator:
            counter_student = 0
            print("Eingabe der Schüler in der KLasse", class_name, "beendet")
            break

        else:
            print("Sie haben der KLasse", class_name, "den Schüler", student_name, "hinzugefügt")
            counter_student += 1
            print("Sie haben", counter_student, "Schüler der Klasse hinzugefügt.")
            list_of_students.append(student_name)

for name_list in list_of_students:
    counter_all_students += 1
    print(str(counter_all_students) + ")", name_list)

print("Sie haben insgesamt", counter_all_students, "Schüler in", counter_class, "Klassen hinzugefügt.")

target_list = list()

while True:
    target = input("Bitte geben Sie den Namen des Schülers ein welchen Sie entfernen wollen: ")

    if target == terminator:
        break

    else:
        student_to_delete = list_of_students.index(target)
        list_of_students.pop(student_to_delete)
        target_list.append(target)

        for x in list_of_students:
            print(x)

print("Sie haben die folgenden Schüler aus den Klassen entfernt: ")
for y in target_list:
    print(y)

number_of_students = len(list_of_students)
print("Sie haben aktuell", number_of_students, "Schüler in Klassenlisten angelegt.")
number_of_deleted_students = len(target_list)
print("Sie haben", number_of_deleted_students, "Schüler aus den Klassenlisten entfernt.")



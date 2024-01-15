
def add_employee(employee_and_salary):
    name = input("Bitte geben Sie den Namen des neuen Mitarbeiters ein: ")

    if name in employee_and_salary:
        print("Ein Mitarbeiter mit diesem Namen ist bereits im Unternehmen.")

        overwrite = input("Möchten Sie das Gehalt ändern? (J/N)?")

        if overwrite == "J" or overwrite == "j":
            salary = float(input("Bitte geben Sie das neue Gehalt ein: "))

            employee_and_salary[name] = salary

        else:
            print("Es werden keine Änderungen am Gehalt vorgenommen.")

    else:
        salary = float(input("Bitte geben Sie das Gehalt des neuen Mitarbeiters ein: "))
        employee_and_salary[name] = salary

def remove_employee(dictionary):
    name = input("Bitte geben Sie den Namen des Mitarbeiters ein den Sie entfernen möchten: ")

    if name in dictionary:
        safety = input("Möchten Sie den Mitarbeiter " + name + " wirklich entfernen? (J/N): ")

        if safety == "J" or safety == "j":
            dictionary.pop(name)
            print("Der Mitarbeiter " + name + " wurde entfernt.")

        else:
            print("Der Mitarbeiter " + name + " wurde nicht etnfernt.")

    else:
        print("Der Mitarbeiter " + name + " ist nicht im Unternehmen und kann daher nicht entfernt werden.")

def sum_of_salarys(employee_and_salary):
    print(sum(employee_and_salary.values()))

def order_salarys(dictionary):
    #print(dict(sorted(dictionary.items(), key=lambda x: x[1])))

    salaries = dictionary.values()
    sorted_salaries = sorted(salaries)

    for salary in sorted_salaries:
        for employee in dictionary.keys():
            if dictionary[employee] == salary:
                print(salary, ":", employee)



employee_and_salary = dict()

employee_and_salary["Franz Mayer"] = 2023.76
employee_and_salary["Kevin Pohl"] = 2.50
employee_and_salary["Hans Petersen"] = 3415.89



order_salarys(employee_and_salary)


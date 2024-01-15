#Übung

age_in_years = input("Bitte geben Sie Ihr Alter ein: ")
age_in_years = int(age_in_years)
if age_in_years <= 12:
    print("Kind")
elif age_in_years > 12 and age_in_years <= 18:
    print("Teenager")
elif age_in_years > 18 and age_in_years <= 67:
    print("Erwachsener")
elif age_in_years > 67:
    print("Rentner")
else:
    print("Fehler #1 (undefiniertes Alter)")


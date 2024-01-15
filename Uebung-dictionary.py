


phonebook = {"Peter Mayer": "0162628326",
              "Franz Huber": "2095674238",
              "Kevin Pohl": "0923652923"}

print(phonebook["Peter Mayer"])

phonebook["Sebastian Krüger"] = "016293652"
phonebook["Sebastian Krüger"] = "017632934"

phonebook.pop("Franz Huber")

print(phonebook)
print(phonebook.keys())
print(phonebook.values())
print(phonebook["Sebastian Krüger"])



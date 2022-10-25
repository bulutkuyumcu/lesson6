# Kullanıcıdan veriler varsaylan olarak string gelir.


print("-----REGISTER FORM-----")
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight: "))

print("REGISTER SUCCESS")
print("Name: {} Surname: {} Age: {} Weight: {}".format(name,surname,age,weight))


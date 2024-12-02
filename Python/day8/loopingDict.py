student = {
    "name" : "Anil",
    "age":25,
    "course":"Python"
}

for key in student:
    print(key)

for value in student.values():
    print(value)

for key,value in student.items():
    print(f"{key}:{value}")
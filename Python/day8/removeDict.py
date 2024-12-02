student = {'name': 'Anil', 'age': 56, 'course': 'Python', 'grade': 'A'}
student.pop("age")
print(student)
student.popitem()
print(student)
del student["course"]
print(student)
student.clear()
print(student)
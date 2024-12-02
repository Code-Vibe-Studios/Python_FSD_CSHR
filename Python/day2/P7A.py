"""
Program to classify a person’s age group using if-elif-else
"""

age = int(input("Enter the age: "))
if age <= 12:
    print("You are a Kid")
elif 13 <= age <= 19:
    print("You are a Teenager")
elif 19 < age <= 65:
    print("You are an adult")
else:
    print("You are a senior")
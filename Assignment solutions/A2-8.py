"""8. Program to check the largest of three numbers using nested if statements"""
from sklearn.linear_model import lars_path

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

# largest = a
#
# if largest < b:
#     largest = b
#
# if largest < c:
#     largest = c

if a >= b:
    if a >= c:
        largest = a
    else:
        largest = c
else:
    if b >= c:
        largest = b
    else:
        largest = c


print(f"{largest} is the largest number.")
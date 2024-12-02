"""
WAPP to find the sum of first n natural numbers using while loop
"""

n = int(input("Enter a positive number: "))
total = 0
i = 1

while i <= n:
    total+=i
    i+=1

print(f"The sum of the first {n} natural numbers is: {total}")
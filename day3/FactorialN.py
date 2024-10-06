# Factorial of a Number 3 = 1*2*3,5=1*2*3*4*5=120

number = int(input("Enter a number: "))  # 3
result = 1                               # 1,1,2,6
for i in range(1,number + 1):            # 1,2,3
    result = result * i                  # 1*1=1,1*2=2,2*3=6

print(f"The factorial of {number} is: {result}") # 3, 6
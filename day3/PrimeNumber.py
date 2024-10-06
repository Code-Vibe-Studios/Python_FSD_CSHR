# Prime Number -> the number which is divisible by 1 and itself is called as prime number
"""
1. take the number as input
2. create a range(2,number) -> 2,3,4
3. check every number in range with input if it is a factor
4. if any number is a factor then you'll say that it is not a prime number
"""
# flag = True
number = int(input("Enter a number: "))
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            # flag = False
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

#
# if flag:
#     print(f"{number} is prime")
# else:
#     print(f"{number} is not prime")

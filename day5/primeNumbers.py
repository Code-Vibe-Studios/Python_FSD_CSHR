"""
1. Find All Prime Numbers Between Two Numbers
2. Find the Nth Prime Number -> 15 == 47
3. Program to Find the Sum of All Prime Numbers Below a Given Number -> 20
"""
def isPrime(start, stop):
    isprime = True
    for j in range(start, stop):
        if num % j == 0:
            isprime=False
            break
    return isprime

l_limit = int(input("enter the lower limit:  "))
u_limit = int(input("enter the upper limit:  "))
for num in range(l_limit,u_limit):
    if isPrime(2,num):
        print(f"{num} is a prime number between {l_limit} and {u_limit}")
#-------------------------------------------------------------------------------------------------
n = int(input("enter the value of N to find the nth prime number: "))
count = 0 # to count the number primes found
num = 2 # start checking from 2 (first prime number)
for num in range(2,99999999):
    if isPrime(2,num):
        count+=1
        if count == n:
            print(f"The {n}th prime number is: {num}")
            break
#--------------------------------------------------------------------------------------------------------
limit = int(input("enter the number to find the sum of all primes below:  "))
prime_sum = 0
for num in range(2,limit):
    if isPrime(2,num):
        prime_sum += num
print(f"{prime_sum} is the sum of all primes below {limit}")
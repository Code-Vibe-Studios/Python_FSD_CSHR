"""2. Find the Nth Prime Number"""

n = int(input("enter the value of N to find the nth prime number: "))

count = 0 # to count the number primes found
num = 2 # start checking from 2 (first prime number)

for num in range(2,99999999):
    is_prime = True

    for j in range(2, num):
        if num % j == 0:
            is_prime=False
            break

    if is_prime:
        count+=1
        if count == n:
            print(f"The {n}th prime number is: {num}")
            break
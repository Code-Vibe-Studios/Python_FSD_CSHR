"""
1. Find All Prime Numbers Between Two Numbers
2. Find the Nth Prime Number -> 15 == 47
3. Program to Find the Sum of All Prime Numbers Below a Given Number -> 20
"""


def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True


def find_primes_between(start, end):
    primes = []
    for num in range(start,end):
        if is_prime(num):
            primes.append(num)
    return primes

def find_nth_prime(n):
    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1


def sum_of_primes_below(limit):
    total = 0
    for num in range(2,limit):
        if is_prime(num):
            total += num
    return total


def main():
    while True:
        print("\n Select an option:")
        print("1. Find all prime numbers between two numbers")
        print("2. Find the nth prime number")
        print("3. Find the sum of all prime numbers below a given number")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            start = int(input("Enter the starting number: "))
            end = int(input("Enter the ending number: "))
            primes = find_primes_between(start,end)
            print(f"Prime numbers between {start} and {end}: {primes}")
        elif choice == 2:
            n = int(input("Enter the nth number: "))
            nth_prime = find_nth_prime(n)
            print(f"The {n}th prime number is : {nth_prime}")
        elif choice == 3:
            limit = int(input("Enter the limit: "))
            prime_sum = sum_of_primes_below(limit)
            print(f"The sum of all prime numbers below {limit} is: {prime_sum}")
        elif choice == 4:
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Please choose between 1 and 4")

main()
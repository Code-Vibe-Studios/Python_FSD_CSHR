

limit = int(input("enter the number to find the sum of all primes below:  "))

prime_sum = 0

for num in range(2,limit):
    is_prime = True

    for j in range(2, num):
        if num % j == 0:
            is_prime=False
            break

    if is_prime:
        prime_sum += num

print(f"{prime_sum} is the sum of all primes below {limit}")
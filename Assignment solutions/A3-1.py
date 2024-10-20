

l_limit = int(input("enter the lower limit:  "))
u_limit = int(input("enter the upper limit:  "))

for num in range(l_limit,u_limit):
    is_prime = True

    for j in range(2, num):
        if num % j == 0:
            is_prime=False
            break

    if is_prime:
        print(f"{num} is a prime number between {l_limit} and {u_limit}")

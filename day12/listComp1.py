# create a list of squares of numbers from 1 to 5
squares = [x**2 for x in range(1,6)]
print(squares)

#create a list of even numbers from 1 to 10
evens = [x for x in range(1,11) if x % 2 == 0]
print(evens)

#Convert C to F only for temperatures above 0
celsius = [-10, 0 ,5, 10, 15]
fahrenheit = [(temp*( 9/5)) + 32 for temp in celsius if temp > 0]
print(fahrenheit)

# Capitalise words in a list
words = ["hello", "world", "python"]
capitalized = [word.upper() for word in words]
print(capitalized)
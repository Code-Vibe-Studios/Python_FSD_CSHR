#Function definition
def greeting():
    print("Hello, Welcome to Python Programming")

#Function call
# greeting()
n = 4 # Global Variables

def greet(name1,name2):
    n = 8   # Local Variable
    print(n)
    print(f"Hello {name1} and {name2}, Welcome to Python Programming")

# greet("Mounish")
# greet(name="Mounish")
a = input("Enter a name: ")
greet("Mounish",a)
print(n)
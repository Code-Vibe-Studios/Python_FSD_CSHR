#basic example
try:
    print(7/2)
except ZeroDivisionError:
    print("Number cannot be divided by 0")
except TypeError:
    print("unsupported operand type(s) for /: 'int' and 'str'")
finally:
    print("Program ended")
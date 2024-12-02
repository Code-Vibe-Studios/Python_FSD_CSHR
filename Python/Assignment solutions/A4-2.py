"""
2. WAPP that keeps asking for a password until the user enters the correct password
"""
correct_password = "python"
entered_password = input("Enter the password")

while entered_password != correct_password:
    print("Incorrect password")
    entered_password = input("Enter the password")

print("Access granted")
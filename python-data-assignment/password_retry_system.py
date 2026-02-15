# Program to repeatedly ask for password until correct

password = ""  # initialize empty string

while password != "admin123":
    password = input("Enter password: ")

print("Access granted")
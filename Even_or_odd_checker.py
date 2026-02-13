# Function definition
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Main code: take input from user
num = int(input("Enter a number: "))

# Call the function and print the result
result = check_even_odd(num)
print("The number is:", result)
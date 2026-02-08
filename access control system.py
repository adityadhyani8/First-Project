# Ask the user for their age
age = int(input("Enter your age: "))

# Ask the user if they have an ID card
has_id_input = input("Do you have an ID card? (True/False): ")

# Normalize and validate the Boolean input
if has_id_input.lower() == "true":
    has_id = True
elif has_id_input.lower() == "false":
    has_id = False
else:
    print("Invalid input for ID card. Please enter True or False.")
    has_id = None

# Check conditions only if ID input was valid
if has_id is not None:
    if age >= 18 and has_id:
        print("Entry allowed")
    else:
        print("Entry denied")
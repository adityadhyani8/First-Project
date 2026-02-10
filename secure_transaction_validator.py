# Ask the user for account balance
account_balance = int(input("Enter your account balance: "))

# Ask the user for withdrawal amount
withdrawal_amount = int(input("Enter withdrawal amount: "))

# Ask the user for verification status
verification_input = input("Are you verified? (True/False): ").strip().lower()

# Convert verification input to Boolean
if verification_input == "true":
    is_verified = True
elif verification_input == "false":
    is_verified = False
else:
    print("Invalid input for verification status. Please enter True or False.")
    is_verified = None

# Check conditions using compound Boolean expressions
if is_verified is not None:
    if is_verified and withdrawal_amount <= account_balance:
        print("Withdrawal successful")
    else:
        print("Transaction denied")
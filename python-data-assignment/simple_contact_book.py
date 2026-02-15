# Create an empty contact book dictionary
contacts = {}

# Ask user to enter at least 3 contacts
num_contacts = int(input("Enter number of contacts (at least 3): "))

if num_contacts < 3:
    print("You must enter at least 3 contacts.")
else:
    for i in range(num_contacts):
        name = input(f"Enter name for contact {i+1}: ")
        phone = input(f"Enter phone number for {name}: ")
        contacts[name] = phone

    # Print all contacts
    print("\nContact Book:")
    for name, number in contacts.items():
        print(f"{name}: {number}")

    # Ask user for a name to search
    search_name = input("\nEnter a name to search: ")

    # Dictionary lookup using 'in' keyword
    if search_name in contacts:
        print(f"Phone number of {search_name}: {contacts[search_name]}")
    else:
        print("Contact not found")

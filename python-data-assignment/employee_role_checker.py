# Main program
def main():
    # Take employee details as input and store in a tuple
    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")
    emp_dept = input("Enter Employee Department: ")

    employee = (emp_id, emp_name, emp_dept)

    # Store employee roles in a set (user input)
    roles = set()
    num_roles = int(input("Enter number of roles: "))
    for i in range(num_roles):
        role = input(f"Enter role {i+1}: ")
        roles.add(role)

    # Print employee info using tuple indexing
    print("\nEmployee Details:")
    print("ID:", employee[0])
    print("Name:", employee[1])
    print("Department:", employee[2])

    # Check whether "admin" exists in roles using set membership
    if "admin" in roles:
        print("Admin Access: Yes")
    else:
        print("Admin Access: No")

# Run the program
if __name__ == "__main__":
    main()

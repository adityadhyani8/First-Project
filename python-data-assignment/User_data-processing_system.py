# Function to calculate average scores for each user
def calculate_average_scores(users):
    averages = {}
    for user in users:
        scores = user["scores"]
        avg = sum(scores) / len(scores) if scores else 0
        averages[user["name"]] = avg
    return averages

# Function to check admin access
def has_admin_access(roles):
    return "admin" in roles

# Main function
def main():
    users = []

    num_users = int(input("Enter number of users: "))

    for i in range(num_users):
        print(f"\n--- Enter details for User {i+1} ---")
        name = input("Enter name: ")

        # Enter scores
        scores = []
        num_scores = int(input(f"Enter number of scores for {name}: "))
        for j in range(num_scores):
            score = int(input(f"Enter score {j+1}: "))
            scores.append(score)

        # Enter roles
        roles = set()
        num_roles = int(input(f"Enter number of roles for {name}: "))
        for k in range(num_roles):
            role = input(f"Enter role {k+1}: ")
            roles.add(role)

        # Store user as dictionary
        user = {
            "name": name,
            "scores": scores,
            "roles": roles
        }
        users.append(user)

    # Calculate averages
    averages = calculate_average_scores(users)

    # Print user info
    print("\n===== User Data Summary =====")
    for user in users:
        print("Name:", user["name"])
        print("Average Score:", averages[user["name"]])
        print("Admin Access:", "Yes" if has_admin_access(user["roles"]) else "No")
        print("-" * 30)

# Run the program
if __name__ == "__main__":
    main()

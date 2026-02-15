# Ask user to enter marks of at least 8 students
marks = []

num_students = int(input("Enter number of students (at least 8): "))

if num_students < 8:
    print("You must enter marks for at least 8 students.")
else:
    for i in range(num_students):
        score = int(input(f"Enter mark for student {i+1}: "))
        marks.append(score)

    # Print the full list
    print("\nAll marks:", marks)

    # Print the first 3 marks using slicing
    print("First 3 marks:", marks[:3])

    # Print the last 3 marks using slicing
    print("Last 3 marks:", marks[-3:])

    # Calculate highest, lowest, and average using built-in functions
    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)

    # Display clean output
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Average:", average)

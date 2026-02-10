# Program: User enters scores as a list in terminal

# Take input from user in list form
scores = eval(input("Enter 5 scores as a list (e.g. [72, 45, 89, 30, 60]): "))

# Process the scores
for score in scores:
    if score < 50:
        print("Fail")
        continue   # skip further processing for failed scores
    print("Pass")
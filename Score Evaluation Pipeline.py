# Student Score Evaluation

# User enters the list directly in terminal
scores = eval(input("Enter scores as a list (e.g., [72, 45, 89, 30, 60]): "))

# Iterate through the list
for score in scores:
    if score < 50:
        print("Fail")
        continue   # skip further processing for failed scores
    print("Pass")
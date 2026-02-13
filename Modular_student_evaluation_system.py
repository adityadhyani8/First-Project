# Function to greet the student
def greet_student(name):
    return f"Hello, {name}"

# Function to calculate number of subjects and average score
def evaluate_scores(scores):
    num_subjects = len(scores)
    average_score = sum(scores) / num_subjects if num_subjects > 0 else 0
    return num_subjects, average_score

# Function to determine pass/fail based on average score
def check_result(average_score):
    if average_score >= 50:
        return "Pass"
    else:
        return "Fail"

# Main function
def main():
    # Input student name
    name = input("Enter student name: ")
    
    # Input scores (comma-separated)
    scores_input = input("Enter scores separated by commas: ")
    scores = [float(score.strip()) for score in scores_input.split(",")]
    
    # Call functions
    greeting = greet_student(name)
    num_subjects, average_score = evaluate_scores(scores)
    result = check_result(average_score)
    
    # Print final result
    print(greeting)
    print("Subjects:", num_subjects)
    print("Average Score:", average_score)
    print("Result:", result)

# Start the program
main()
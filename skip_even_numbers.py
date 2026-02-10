# Program: Print numbers from 1 to 10, skipping even numbers

for num in range(1, 11):
    if num % 2 == 0:   # check if number is even
        continue       # skip even numbers
    print(num)
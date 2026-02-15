# Program: Print first number divisible by 7 (from 1 to 50)

for num in range(1, 51):
    if num % 7 == 0:
        print(num)
        break
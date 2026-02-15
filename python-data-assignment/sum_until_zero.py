# Program: Keep asking numbers until user enters 0

total = 0  # initialize sum

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break   # stop loop when user enters 0
    total += num

print("Total:", total)
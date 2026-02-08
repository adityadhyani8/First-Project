# Sum until 0 is entered

total = 0  # initialize sum

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break   # exit loop when 0 is entered
    total += num

print("Total:", total)
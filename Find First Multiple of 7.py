# First number divisible by 7

for num in range(1, 51):
    if num % 7 == 0:
        print(num)
        break   # exit the loop once found
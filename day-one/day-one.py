file = open("input.txt", "r");

total = 0;
numbers = []

for line in file:
    for char in line:
        if char.isdigit():
            numbers.append(char)
    lineTotal = str(numbers[0]) + str(numbers[-1])
    total += int(lineTotal)
    numbers.clear()

print (total);
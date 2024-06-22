import sys

file = open(sys.argv[1], "r")
numbers = [int(number.strip()) for number in file.readlines()]
file.close()
sr = round(sum(numbers) / len(numbers))

result = 0
for number in numbers:
    if number > sr:
        result += number - sr
    elif number < sr:
        result += sr - number
print(result)

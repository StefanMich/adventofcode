total = 0

with open('day_1_input') as f:
    input_strings = f.read()

for line in input_strings.split('\n'):
    if not line:
        continue

    operator = line[0]
    number = int(line[1:])

    if operator == '+':
        total += number
    else:
        total -= number

print(total)

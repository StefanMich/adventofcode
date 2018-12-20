total = 0
frequencies = set()

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

    if total in frequencies:
        print(total)
        exit(0)
    else:
        frequencies.add(total)

print(total)

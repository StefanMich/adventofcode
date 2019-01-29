def react_polymer(polymer):
    previous_length = len(polymer)
    while True:
        print(previous_length)
        pairs = list(react_iteration(polymer))
        polymer = reaction_to_string(pairs)
        new_length = len(polymer)
        if new_length == previous_length:
            break
        previous_length = new_length

    result = reaction_to_string(polymer)
    return result


def reaction_to_string(reaction):
    result = ''.join(reaction)
    return result


def react_iteration(polymer):
    STOP = '|'
    padded_polymer = polymer + STOP
    total_pairs = len(padded_polymer) - 1

    remove_next = False
    for pair in range(total_pairs):
        first, second = padded_polymer[pair:pair+2]
        if remove_next:
            remove_next = False
            continue
        if first.lower() == second.lower():
            if first != second:
                remove_next = True
                continue
        yield first


if __name__ == '__main__':
    with open('input') as input_file:
        input_string = input_file.read()
        print(len(react_polymer(input_string)))

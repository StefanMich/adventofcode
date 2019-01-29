def react_polymer(polymer):
    previous_length = None
    while True:
        pairs = list(zip(polymer, polymer[1:]))
        pairs = list(react_iteration(pairs))
        polymer = reaction_to_string(pairs)
        new_length = len(polymer)
        if new_length == previous_length:
            break
        previous_length = new_length


    result = reaction_to_string(pairs)
    return result


def reaction_to_string(reaction):
    try:
        unzip = list(zip(*reaction))

        try:
            beginning = unzip[0]
        except IndexError:
            beginning = ()

        try:
            ending = (unzip[1][-1],)
        except IndexError:
            ending = ()

        result = beginning + ending
        result = ''.join(result)
    except StopIteration:
        result = ''
    return result


def react_iteration(pairs):
    omit = False
    for pair in pairs:
        if omit:
            omit = False
            continue
        if pair[0].lower() == pair[1].lower():
            if pair[0] != pair[1]:
                omit = True
                continue
        yield pair

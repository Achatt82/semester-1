# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'

def Generate(size):
    sequence = [0]
    for i in range(1, size):
        prev = sequence[i - 1]
        cache = prev - i
        if (cache > 0 and cache not in sequence):
            sequence.append(cache)
        else:
            sequence.append(prev + i)

    return sequence


# You may wish to use further output for testing purposes while you develop your code

sequence = Generate(L)

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence
def ReverseCompliment(pattern):
    compliment_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    compliment = []
    for char in pattern:
        compliment.append(compliment_map.get(char))

    return ''.join(i for i in compliment)[::-1]


print(ReverseCompliment("ATGATCAAG"))

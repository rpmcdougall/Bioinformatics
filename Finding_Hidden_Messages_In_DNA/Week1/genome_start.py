def GenomePositions(Pattern, Genome):
    positions = []
    for i in range(len(Genome) - len(Pattern) + 1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return ' '.join([str(pos) for pos in positions])


print(GenomePositions("ATGATCAAG", open("Vibrio_cholerae.txt", "r").read()))

def genome_skew(genome):
    minimum_skew = []
    skew_plot = []
    skew_map = {'A': 0, 'T': 0, 'G': 1, 'C': -1}
    skew_plot.append(0)
    skew_value = 0
    for i in range(1, len(genome)):
        skew_value += skew_map.get(genome[i])
        skew_plot.append(skew_value)

    minimum = min(skew_plot)
    for i in range(0, len(skew_plot)):
        if skew_plot[i] == minimum:
            minimum_skew.append(i + 1)

    return minimum_skew


# d = open("Salmonella_enterica.txt").readlines()
# d = d[1:-1]
# print(genome_skew("".join(map(str.strip, d))))

def genome_skew_max(genome):
    minimum_skew = []
    skew_plot = []
    skew_map = {'A': 0, 'T': 0, 'G': 1, 'C': -1}
    skew_plot.append(0)
    skew_value = 0
    for i in range(1, len(genome)):
        skew_value += skew_map.get(genome[i])
        skew_plot.append(skew_value)

    minimum = max(skew_plot)
    for i in range(0, len(skew_plot)):
        if skew_plot[i] == minimum:
            minimum_skew.append(i + 1)

    return minimum_skew


print(genome_skew_max("CATTCCAGTACTTCATGATGGCGTGAAGA"))

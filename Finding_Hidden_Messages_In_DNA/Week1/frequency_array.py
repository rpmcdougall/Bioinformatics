
def SymbolToNumber(symbol):
    symbol_map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    return symbol_map.get(symbol)


def NumberToSymbol(symbol):
    symbol_map = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    return symbol_map.get(symbol)

# TODO: This isn't even close, read the prompt dummy


def NumberToPattern(Number):
    pattern = []
    for char in str(Number):
        pattern.append(NumberToSymbol(int(char)))
    return ''.join([str(x) for x in pattern])


def PatternToNumber(Pattern):
    if Pattern == "":
        return 0
    symbol = Pattern[-1]
    Prefix = Pattern[0:-1]
    return 4 * PatternToNumber(Prefix) + SymbolToNumber(symbol)


def ComputingFrequencies(Text, k):
    frequency_array = []
    for i in range(0, 4 ** k):
        frequency_array.append(0)
    for i in range(0, len(Text) - k + 1):
        Pattern = Text[i: i + k]
        j = PatternToNumber(Pattern)
        frequency_array[j] = frequency_array[j] + 1
    return frequency_array


def ClumpFinding(Genome, k, L, t):
    FrequentPatterns = []
    Clump = []
    for i in range(0, 4 ** k - 1):
        Clump.append(0)
    for i in range(0, len(Genome) - L):
        Text = Genome[i: i + L]
        FrequencyArray = ComputingFrequencies(Text, k)
        for j in range(0, 4 ** k - 1):
            if FrequencyArray[j] >= t:
                Clump[j] = 1
    for i in range(0, 4 ** k - 1):
        if Clump[i] == 1:
            FrequentPatterns.append(NumberToPattern(i, k))
    return FrequentPatterns


print(NumberToPattern("5437"))

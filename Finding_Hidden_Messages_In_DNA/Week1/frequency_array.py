
def SymbolToNumber(symbol):
    symbol_map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    return symbol_map.get(symbol)


def NumberToSymbol(symbol):
    symbol_map = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    return symbol_map.get(symbol)

def NumberToPattern(index, k):
    if k == 1:
        return NumberToSymbol(index)
    prefix_index, r = divmod(index, 4)
    symbol = NumberToSymbol(r)
    prefix_pattern = NumberToPattern(prefix_index, k - 1)
    return prefix_pattern + symbol


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
    Text = Genome[0:L]
    FrequencyArray = ComputingFrequencies(Text, k)
    for i in range(0, 4 ** k - 1):
        if FrequencyArray[i] >= t:
            Clump[i] = 1
    for i in range(1, len(Genome) - L):
       FirstPattern = Genome[i-1:i -1 + k]
       index = PatternToNumber(FirstPattern)
       FrequencyArray[index] = FrequencyArray[index] - 1
       LastPattern = Genome[i+L-k:i + L]
       index = PatternToNumber(LastPattern)
       FrequencyArray[index] = FrequencyArray[index] + 1
    for i in range(0, 4 ** k - 1):
        if Clump[i] == 1:
            FrequentPatterns.append(NumberToPattern(i, k))
    return FrequentPatterns


print(len(ClumpFinding(open("E_coli.txt", "r").read(), 9, 500, 3)))

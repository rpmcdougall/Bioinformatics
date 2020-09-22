def hamming_distance(p, q):
    mismatches = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            mismatches += 1

    return mismatches


def PatternCount(text, pattern, d):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        mismatches = hamming_distance(text[i:i+len(pattern)], pattern)
        if mismatches <= d:
            count = count + 1
    return count


print(PatternCount("CATGCCATTCGCATTGTCCCAGTGA", "CCC", 2))

def hamming_distance(p, q):
    mismatches = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            mismatches += 1

    return mismatches


print(hamming_distance("CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT",
                       "CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG"))

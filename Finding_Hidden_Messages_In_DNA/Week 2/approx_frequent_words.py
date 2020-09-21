import operator

def hamming_distance(p, q):
  mismatches = 0
  for i in range(len(p)):
    if p[i] != q[i]:
      mismatches += 1
      
  return mismatches
  

def Neighbors(Pattern, d):
  if d == 0:
    return [Pattern]
  if len(Pattern) == 1:
    return ['A', 'C', 'G', 'T']
  Neighborhood = []
  SuffixNeighbors = Neighbors(Pattern[1:], d)
  for value in SuffixNeighbors:
    if hamming_distance(Pattern[1:], value) < d:
      for x in ['A', 'C', 'G', 'T']:
        Neighborhood.append(x + value)
    else:
      Neighborhood.append(Pattern[0]+value)
  return Neighborhood

def PatternCount(text, pattern, d):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        mismatches = hamming_distance(text[i:i+len(pattern)], pattern)
        if mismatches <= d:
            count = count + 1
    return count

def FrequentWords(text, k, d):
    frequent_patterns = []
    count = []
    frequency_map = {}
    
   
    
    for i in range(len(text) - k):
        pattern = text[i:i+k]
        pattern_neighbors = Neighbors(pattern, d)
        pattern_neighbors.append(pattern)
        print(pattern)
        for p in pattern_neighbors:
          occurences = PatternCount(text, p, d)
          frequency_map[p] = occurences
          count.append(occurences)
    
    print(count)
    max_value = max(count)
    print(max_value)
    for pattern, value in frequency_map.items():
      if value == max_value:
        frequent_patterns.append(pattern)

    return set(sorted(frequent_patterns))
    
print(FrequentWords("AAT", 3, 0))


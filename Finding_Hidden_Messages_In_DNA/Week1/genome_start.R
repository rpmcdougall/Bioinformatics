#def GenomePositions(Pattern, Genome):
#  positions = []
#  for i in range(len(Genome) - len(Pattern) + 1):
#    if Genome[i:i+len(Pattern)] == Pattern:
#    positions.append(i)
#  return ' '.join([str(pos) for pos in positions])
# print(GenomePositions("ATGATCAAG", open("Vibrio_cholerae.txt", "r").read()))
library(readr)

genome_start <- function(pattern, genome) {
  positions <- vector()
  for (i in nchar(genome):nchar(pattern)){
    if(substr(genome, i, i+nchar(pattern) -1) == pattern) {
      positions <- c(positions, i)
    }
  }
  return(positions)
}


genome_start("ATGATCAAG", read_file("Vibrio_cholerae.txt"))
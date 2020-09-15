#install.packages("reader")
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
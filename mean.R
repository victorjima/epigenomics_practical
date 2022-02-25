##################
# OPTION PARSING #
##################

suppressPackageStartupMessages(library("optparse"))

option_list <- list (
  
  make_option ( c("--input"),
                help = "tsv file" ),
  
  make_option ( c("--column"),
                help = "column from which the mean will be returned" )
  
)


parser <- OptionParser(
  usage = "%prog [options]",
  option_list=option_list,
  description = "\nMean of a selected column"
)

arguments <- parse_args(parser, positional_arguments = TRUE)
opt <- arguments$options


##################
# COMPUTE MEAN   #
##################

# Read tsv
tsv <- read.table(file = opt$input, sep = '\t')

# Compute mean
mean <- mean(tsv[,as.integer(opt$column)])

# Output
print(mean)

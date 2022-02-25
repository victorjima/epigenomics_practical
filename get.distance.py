#!/usr/bin/env python


#************
# LIBRARIES *
#************

import sys
from optparse import OptionParser


#*****************
# OPTION PARSING *
#*****************

parser = OptionParser()
parser.add_option("-i", "--input", dest="input")
parser.add_option("-s", "--start", dest="start")
options, args = parser.parse_args()

open_input = open(options.input)
enhancer_start = int(options.start)


#********
# BEGIN *
#********

x=1000000 # set maximum distance to 1 Mb
selectedGene="" # initialize the gene as empty
selectedGeneStart=0 # initialize the start coordinate of the gene as empty

for line in open_input.readlines(): # for each line in the input file
    gene, position = line.strip().split('\t') # split the line into two columns based on a tab
    # gene variable corresponds to the ID of the gene
	# position variable corresponds to the start of the gene
    difference = abs(int(position) - enhancer_start) # compute the absolute value of the difference between position and enhancer_start
    if difference < x: # if this absolute value is lower than x
        x = difference # this value will now be your current x
        selectedGene = gene # save gene as selectedGene
        selectedGeneStart = position 	# save position as selectedGeneStart
	

print("\t".join([selectedGene, str(selectedGeneStart), str(x)]))

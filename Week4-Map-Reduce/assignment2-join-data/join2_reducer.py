#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This reducer code will input <show, viewer_count> and <show, channel>
#input files and return viewer counts for tv shows that air on ABC.
# Note the input will come as a group of lines with same show (ie the key)
# As it reads words it will hold on to the value field
#
# It will keep track of current show and previous show, if show changes
#   then it will perform the 'join' on the set of held values by merely printing out 
#   the word and values.  In other words, there is no need to explicitly match keys b/c
#   Hadoop has already put them sequentially in the input 
#   
# At the end it will perform the last join
#
#
#  Note, there is NO error checking of the input, it is assumed to be correct, meaning
#   it has word with correct and matching entries, no extra spaces, etc.
#
#  see https://docs.python.org/2/tutorial/index.html for python tutorials
#
#  San Diego Supercomputer Center copyright
# --------------------------------------------------------------------------

prev_show          = " "                #initialize previous show to blank string

flag_abc             = 0 #indicate shows on abc
viewer_count         = 0 

line_cnt           = 0  #count input lines
curr_show          = " "
for line in sys.stdin:
    line       = line.strip() 
    key_value  = line.split('\t')
    line_cnt   = line_cnt+1     

    curr_show, value_in  = key_value  

    if curr_show != prev_show:
        if line_cnt > 1 and flag_abc==1:
	          print('{0} {1}'.format(prev_show,viewer_count))

	  flag_abc = 0
    viewer_count = 0
    prev_show = curr_show  #set up previous show for the next set of input lines

    if value_in == 'ABC': 
        
        flag_abc = 1

    else:

        viewer_count += int(value_in)

print('{0} {1}'.format(curr_show,viewer_count))

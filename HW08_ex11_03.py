#!/usr/bin/env python
# Exercise 3  
# Dictionaries have a method called keys that returns the keys of the 
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical 
# order.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
##############################################################################

def print_hist_old(h):
    for c in h:
        print c, h[c]


def print_hist_new(h):
    for key, value in sorted(h.items()): 
        print(key, value)
#     d = dict()
#     for key in sorted(h.iterkeys()):
#         print key
# #     for key.lower(), value in h.items():
# #         print(key, value)
# #         new_key = key.lower()
# #         d[new_key] = value
#         
    
    

##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 BELOW: ##################
##############################################################################

def histogram_new(pledge_list):
    pledge_histogram = dict()
    for c in pledge_list:
        pledge_histogram[c] = 1 + pledge_histogram.get(c, 0)
    return pledge_histogram

def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in 
    the order it appears in the original file. returns the list.
    """
    with open("pledge.txt") as f :
        pledge_list = []
        for line in f:
            words = line.replace(':',' ').replace(',',' ').replace('.',' ').split()   #replace all special characters with the space 
            #and split line at space
            pledge_list += words
        
        return histogram_new(pledge_list)
#                     
        

##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
##############################################################################
def main():
    """ Calls print_hist_new with the appropriate arguments to print the 
    histogram of pledge.txt.
    """
    print_hist_new(get_pledge_list())

if __name__ == '__main__':
    main()

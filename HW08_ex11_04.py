#!/usr/bin/env python
# Exercise 4  
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.
# from HW08.HW08_ex11_02 import pledge_histogram, histogram_new, get_pledge_list

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
##############################################################################
def reverse_lookup_old(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError

def reverse_lookup_new(pledge_histogram, v):
    key_list = []
    for k in pledge_histogram:                  #parse each key of dictionary 
        if str(pledge_histogram[k]) == v:
            key_list.append(k)
    return key_list
        


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
#             for word in words:
#                 word_list.append(word)        
        return pledge_list



##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
def main():   # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    print reverse_lookup_new(pledge_histogram, "1")
    print reverse_lookup_new(pledge_histogram, "9")
    print reverse_lookup_new(pledge_histogram, "Python")

if __name__ == '__main__':
    main()

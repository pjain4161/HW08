#!/usr/bin/env python
# mimsmind0
#Version 0: Basic Feedback (High/Low)

# In this version, the program generates a random number with number of digits equal to length.
# If the command line argument length is not provided, the default value is 1.
# Then, the program prompts the user to type in a guess, 
# informing the user of the number of digits expected. 
# The program will then read the user input, and provide basic feedback to the user. 
# If the guess is correct, the program will print a congratulatory message 
# with the number of guesses made and terminate the game. 
# Otherwise, the program will print a message asking the user to 
# guess a higher or lower number, and prompt the user to type in the next guess. 
################################################################################


#Imports
###############################################################################################################
from random import randint
import sys
from _random import Random



#body
######################################################################################################
#get_number(digits)
#This function prompts the user to type in a guess, informing the user of the number of digits expected
#######################################################################################################
def get_number(digits):
    num = raw_input("\nGuess a {0}-digit number:  " .format(digits))
    return num


######################################################################################################
# get_random_number(No_of_digits)
#This function creates randon number
#######################################################################################################
def get_random_number(No_of_digits):
    random_number = ""
    for n in range(No_of_digits):
        random_number  += str(randint(0,9))
    return random_number
    
    
########################################################################################################
# maximum_rounds(length)
#This function generates maximum number of rounds that user can try
#########################################################################################################
def maximum_rounds(length):
    return  ((2**length) + length)


########################################################################################################
# bulls_and_cows_feedback(user_num, random_num, count)
# This function reads the user input and provides bulls and cows feedback to the user. 
#A matching digit in the correct position will result in a bull, 
#while a matching digit in the wrong position will result in a cow
########################################################################################################
def bulls_and_cows_feedback(user_num, random_num):
    bull = 0
    cow = 0
    #calculating individual digits in the number entered by the user and random number and comparing them
    for u in range(len(user_num)) :             # run loop for each digit in user number
        list_of_digits_counted = []
        for r in range(len(random_num)):        # run loop for each digit in random number
            instance_counted  = False
            if u == r:                          # if index positions are same and digits at these positions are also same, increment bull by one
                if user_num[u] == random_num[r]:
                    bull += 1
                    instance_counted = True
                    list_of_digits_counted.append(user_num[u]) # List to add occurances of all digits till now
                    
        if (instance_counted == False )  and  (user_num[u] not in list_of_digits_counted) and  (user_num[u] in random_num):
            cow += 1
            
    values = [bull, cow]
    return values

########################################################################################################
# match(user_num,random_num, count)
#This function prints a congratulatory message or asks for user input
#########################################################################################################
def match(user_num,random_num, count):
    if (user_num == random_num):
        if (count == 1):
            print "\nCongratulations. You guessed the correct number in %s try" %(count)
        else:
            print "\nCongratulations. You guessed the correct number in %s tries" %(count)
        exit(0)
    else:
        values = bulls_and_cows_feedback(user_num, random_num)
        
    return values
 
####################################################################################################################
def main():     
    # If the command line argument length is not provided, the default value is 3
    if len(sys.argv) == 1:
            No_of_digits = 3
    else:
        try:
        # If the command line argument is not a numeric value, an error message is displayed and program exits.
            check = eval(sys.argv[1]) 
        except:
            print "\nYou gave a wrong input. Game over"
            exit(0)
        else:
            No_of_digits = int(sys.argv[1].strip())
    
#     Generating a random Number with No_of_digits
    random_number = get_random_number(No_of_digits)
    
    #generating maximum number of rounds
    maxrounds = maximum_rounds(No_of_digits)
    
    print "\nLet's play the mimsmind1 game. You have {number_of_guess} guesses" .format(number_of_guess = maxrounds)
    
    #getting user input
    user_number = get_number(No_of_digits)
    
    #initialising counter
    count = 1   
    
    while (count < maxrounds):
        #check if user has entered any input other than a numeric value and handle the exception
        try:
            user_int = int(user_number)    
        except:
            user_number = raw_input("\nInvalid input. Try again: ")
            continue
        else:
            #check if the input entered by user is in the expected range
            if (len(user_number) < No_of_digits) or len(user_number) > No_of_digits:
                user_number = raw_input("\nInvalid input. Try again: ")
                continue

            else:
                values = match(user_number, random_number, count)      
                user_number = raw_input("\n{0} bull(s), {1} cow(s). Try again: " .format(values[0], values[1]))
                count = count + 1
   
    values = match(user_number, random_number, count) 
   
    #if the user exceeds the maximum number of tries allowed,then print an
    #apologetic message with the number of guesses made, and terminate the game.
    print "\nSorry. You did not guess the number in {0} tries. The correct number is {1}" .format(count, random_number)

#################################################################################################################

if __name__ == '__main__':
    main()
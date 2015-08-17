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

###############################################################################################################
#                                             Imports
##############################################################################################################
from random import randint
import sys
##############################################################################################################


###############################################################################################################
#                                             Body
######################################################################################################

######################################################################################################
# get_number(digits)
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
# match(user_num,random_num, count)
#This function prints a congratulatory message or asks for user input
#########################################################################################################
def match(user_num,random_num, count):
    if (int(user_num) == int(random_num)):
        if (count == 1):
            print "\nCongratulations. You guessed the correct number in %s try" %(count)
        else:
            print "\nCongratulations. You guessed the correct number in %s tries" %(count)
        exit(0)
    else:
        if (int(user_num) < int(random_num)):
            num = raw_input("\nTry again. Guess a higher number: ")
        else:
            num = raw_input("\nTry again. Guess a lower number: ")
        return num
 


#################################################################################################################
def main():
    #############################################################################################################
    ################               checks and initialisations                #####################################
    #############################################################################################################
    
    # If the command line argument length is not provided, setting the default value as 1
    if len(sys.argv) == 1:
            No_of_digits = 1
    else:
        try:
        # If the command line argument is not a numeric value, an error message is displayed and program exits.
            check = eval(sys.argv[1]) 
        except:
            print "\nInvalid input. Start again"
            exit(0)
        else:
            No_of_digits = int(sys.argv[1].strip())     # strip() is added to cater the case of a digit followed by space eg."2 "
    
    #Generating a random Number with No_of_digits
    random_number = get_random_number(No_of_digits)  
    
    ######### Game Starts from here #######################################################################
        
    print "\nLet's play the mimsmind0 game"
    
    #getting user input
    user_number = get_number(No_of_digits)
    
    #initialising counter
    count = 1   
    
    while (True):
        #check to see if user entered any input other than a numeric value and handle the exception
        try:
            user_int = int(user_number)    
        except:
            user_number = raw_input("\nInvalid input. Try again: ")
            continue
        else:
            #check to see if user input is in expected range
            if (len(user_number) < No_of_digits) or len(user_number) > No_of_digits:
                user_number = raw_input("\nInvalid input. Try again: ")
                continue

            else:
                count = count + 1
                user_number = match(user_number, random_number, count)
                

#################################################################################################################

if __name__ == '__main__':
    main()
# Roman Rodriguez, Joshua DeLosSantos, Arturo Verdugo
# Team Saber
# CSE 5408
# Spring 2021
# Lab 4
# a.) reverse a user inputted string

toReverse = ''

print('input a string to be reversed')

toReverse = input()

print(''.join(reversed(toReverse))) #reverse the whole string and printed

                                    #''.join allows for the reversed text to be displayed
                                    #going over, '<reversed object at (some hex)>' message



# Roman Rodriguez, Joshua DeLosSantos, Arturo Verdugo
# Team Saber
# CSE 5408
# Spring 2021
# Lab 4
# e.) Fibonnaci sums

import time

counter = 0
fibon = 0
prevFibon = 1

showP = True     #showP = show prevFibon
showF = False     #showF = show fibon

print('input number to give fibonacci sum:')

string = input()

userNumber = int(string)

if userNumber == 0:         #nothing to add
    print('0')

#begin summing the fibonnaci, the sum of previous to the next sum

else:
    while counter != userNumber:

        showP = not(showP)  #interchanging which sum is done
        showF = not(showF)

        if showP:
            fibon = fibon + prevFibon   #the first sum
            #print('fibon = ', fibon)

        else:
            if showF:
                prevFibon = prevFibon + fibon   #adding from previous
                #print('prevfibon = ', prevFibon)

        counter = counter + 1
        #print('iteration///////////////')  #used to visualize iteration of while loop
        
if showP:
    print('Fibonacci value = ', fibon) #gives previous fibon

if showF:
    print('Fibonacci value = ', prevFibon) #gives newer fibon added from fibon



# Joshua DeLosSantos, Roman Rodriguez, Arturo Verdugo
# Team Saber
# CSE 5408
# Spring 2021
# Lab 4
# b.) check inputted # is prime

num = int(input("Enter a number you want to check: "))

if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print("Your number is not a prime number")
           break
   else:
       print("Your number is a prime number")
       
else:
   print("Your number is not a prime number")



# Joshua DeLosSantos, Roman Rodriguez, Arturo Verdugo
# Team Saber
# CSE 5408
# Spring 2021
# Lab 4
# c.) convert time to military time

def regtoMil(usrin):

    if len(tim2mil) != 7:
        return("Incorrect format")
      
    if usrin[-2:] == "AM" and usrin[:2] == "12": 
        return "00" + usrin[2:-2] 
          
    elif usrin[-2:] == "AM": 
        return usrin[:-2]
    
    elif usrin[-2:] == "PM" and usrin[:2] == "12": 
        return usrin[:-2] 
          
    else: 
        return str(int(usrin[:2]) + 12) + usrin[2:5] 



tim2mil = str(input("Enter your time in the following format '01:30AM' \n"))

print(regtoMil(tim2mil)) 



# Arturo Verdugo, Joshua DeLosSantos, Roman Rodriguez
# Team Saber
# CSE 5408
# Spring 2021
# Lab 4
# e.) good password or not

import time
username = input("Please enter the desired username")
i = 0
while i < 1:
	letters = 0
	digits = 0
	special = 0
	password = input("Please enter the desired password.\n(Must be 7 or more characters, with 2 characters being numbers or special characters.) \n")
	for j in range(len(password)):
		if(password[j].isalpha()):
			letters = letters + 1
		elif(password[j].isnumeric()):
			digits = digits + 1
		else:
			special = special + 1
	if(digits + special) > 1 and len(password) > 6:
		i = 1
		print("# of letters = " + str(letters) + "\n# of digits = " + str(digits) + "\n# of special characters = " + str(special) + "\n Account and Password successfully created. The program will exit in 5 seconds.")
		time.sleep(5)

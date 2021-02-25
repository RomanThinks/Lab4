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


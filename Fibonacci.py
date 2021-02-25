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

showP = 1     #showP = show prevFibon
showF = 0     #showF = show fibon

print('input number to give fibonacci sum:')

string = input()

userNumber = int(string)

if userNumber == 0:
    print('0')

#begin summing the fibonnaci, the sum of previous to the next sum

else:
    while counter != userNumber:
        
        fibon = fibon + prevFibon
        prevFibon = prevFibon + fibon
        
        print('prevFibon = ', prevFibon)
        print('fibon = ', fibon)
        
        showP = ~showP
        showF = ~showF
        
        if showP == 1:
            print(prevFibon)
            counter = counter + 1
            
        if showF == 1:
            print(fibon)
            counter = counter + 1


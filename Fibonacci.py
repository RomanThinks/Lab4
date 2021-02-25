# Roman Rodriguez, Joshua DeLosSantos, Arturo Verdugo
# Team Saber
# CSE 5408
# Spring 2021
# Lab 4
# e.) Fibonnaci sums

counter = 0
counter1 = 0
counter2 = 1
fibon = 0

print('input number to give fibonacci sum:')

string = input()

userNumber = int(string)

#begin summing the fibonnaci, the sum of previous to the next sum

while counter != userNumber+1:
    #counter starts at zero
    fibon = counter1 + counter2
    counter1 = counter1 + 1
    counter2 = counter2 + 1
    
    counter = counter + 1

print(fibon)
    

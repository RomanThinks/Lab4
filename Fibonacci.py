# Roman Rodriguez, Joshua DeLosSantos, Arturo Verdugo
# Team Saber
# CSE 5408
# Spring 2021
# Lab 4
# e.) Fibonnaci sums

counter = 0
fibon = 0
prevFibon = 1

print('input number to give fibonacci sum:')

string = input()

userNumber = int(string)

if userNumber == 0:
    print('0')

#begin summing the fibonnaci, the sum of previous to the next sum

else:
    while counter != userNumber+1:
        #counter starts at zero
    
        fibon = fibon + prevFibon
    
        prevFibon = prevFibon + fibon
        
        print(fibon)
    
    
        counter = counter + 1

    #print(fibon)
    

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

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

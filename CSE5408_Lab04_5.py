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

import sys
password = "changeme"
counter = 0


while counter < 5:
    counter = counter + 1
    guess = input("Please enter the password: ")
    if guess == password:
        print ("Accepted!")
        sys.exit() #sys.exit() will quit the program.
    elif guess != password and counter == 5:
        input("Access denied, please press enter to exit and contact security to reset your password!")
    elif guess != password and counter == 4:
        print("Keep trying, but this is your last attempt, be careful!")
    else:
        print ("Keep trying")
        print ("This is your attempt %d and you still have %d attempts left!" % (counter, 5 - counter))
    


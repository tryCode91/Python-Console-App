from RemoveString import getParamsAndValidate, removePartOfString
from pwdgen import GeneratePassword
from user import database
from validate import validateString, validateInteger
from functions import sleep
import time

# instance of class
dbclass = database()

# Function prints menu
def runProgram(): 
    while True:
        
        choice1 = input("\nWelcome To Petrus Program. Your choices are\n\n1. Remove Part Of String\n2. Generate password\n3. Create User\n4. Show All Users\n5. Show One User \n\n6. Exit\n>")
        
        choice2 = validateInteger(choice1)

        if choice2 != 0:
            print("Please Enter a Number!")
            sleep(1)
            exit()
        else:
            choice1 = int(choice1)

        if choice1 == 1:
            
            val = getParamsAndValidate()
            string = val[0]
            removeLen = val[1]
            result = removePartOfString(string, removeLen)
            print("Resulting string: ", result)
            sleep(3)

        if choice1 == 2:
                        
            pwdlen1 = input("How long would you like the password to be? (1-91 characters): ")
            pwdlen2 = validateInteger(pwdlen1)

            if pwdlen2 != 0:
                print("Please Enter a number...")             
                sleep(2)
                exit()
            
            opt1 = input("Would you like include numbers and symbols in the password?(Yes/No): ")
            opt2 = validateString(opt1)

            if opt2 == 0:
                
                pwdlen1 = int(pwdlen1)
                
                if opt1.lower() == "yes":
                    result = GeneratePassword(pwdlen1, 1)
                elif opt1.lower() == "no":
                    result = GeneratePassword(pwdlen1, 0)
                else:
                    print("Please Enter Yes or No...")
                    sleep(1)
            elif opt2 == 1:
                print("Please enter a number...")
                sleep(1)
            elif opt2 == 2:
                print("Password Can Be Maximum 91 characters long...")
                sleep(1)

            if result:
                print(f'\nYou New Password has been generated: {result}')
                sleep(3)
            else:
                print("Password was not generated")

        elif choice1 == 3:

            name = input("Enter Your Name: ")
            resname = validateString(name)
            
            if resname == 1:
                print("Name must be less than 50 characters long...")
                time.sleep(1)
            elif resname == 2:
                print("Name must be a string!")
                sleep(1)
            
            age = input("Enter Your Age: ")
            resage = validateInteger(age)
                
            if resage == 0:
                database.CreateUser(name, age, (GeneratePassword(5, 0)))
                print("Your user has been created.")
                sleep(1)
            elif resage == 1:
                print("Age can be up to 120 years old.")
                sleep(1)
            elif resage == 2:
                print("Age must be a number!")
                sleep(1)
            
        elif choice1 == 4:
            print("Showing all users")
            sleep(0.5)
            print(database.ShowAllUsers())
            input("Press Enter To Continue...")
        
        
        elif choice1 == 5:
            users = database.CheckRows()
            
            rowid = input("Enter ID for the user that you would like to view: ")
            
            rowidClean = validateInteger(rowid)

            if int(rowid) < users:
                    
                if rowidClean == 0:
                    sleep(0.5)
                    print(database.showOneUser(rowid))
                    input("Press Enter To Continue...")
                else:
                    # Count all rows
                    print("Please enter an number between (1-10)")
                    sleep(2)
            else:
                print(f'Please enter an ID number between 0 and {users}')
                sleep(2.5)

        elif choice1 == 6:
            print("Exiting program...")
            sleep(0.5)
            exit()

        elif choice1 < 1 or choice1 > 6:
            print("Please enter a number between 1-4")
            sleep(1)

runProgram()
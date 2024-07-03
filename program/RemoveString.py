# Getting and setting value
from functions import sleep
def getParamsAndValidate():
    
    string = input("\nEnter a string: ")
    if len(string) >= 100:
        print("String to long. Max 100 characters")
        sleep(2)
    else:    
        removeLen = input("Enter length to remove: ")
        try:
            int(removeLen)
        except:
            print("length has to be a number")
            sleep(2)

        if int(removeLen) > len(string):
            print("Length to remove can be up to: ", len(string), " characters in length.")
            sleep(2)
            
        return string, int(removeLen)

# Function removes n char from the left to right 
def removePartOfString(string, n):
    
    list_string = []

    # store the new string here
    new_list_string = []
    
    # new index to keep from from the old list
    index = 0

    # result
    new_string = ""

    # put every character in list
    for letter in string:
        list_string.append(letter)

    # get the new length
    index = len(list_string) - n

    #only keep the characters from n and up 
    for i in range(len(list_string)):
        if i >= n:
            new_list_string.append(list_string[i])

    for letter in new_list_string:
        new_string += letter    
    
    return new_string
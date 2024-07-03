import random
def GeneratePassword(pwdlen, include):

    if pwdlen > 0 and pwdlen < 92:
        # Include alphabet
        alphabetIsSmall = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        # Include captial letters
        alphabetIsBig = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        # Include numbers 1-9
        numbersArray = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        # Include symbols
        symbolsArray = ['~', '`', '!', '@', '#', '$', '%' ,'^', '&','*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', "'\'", ':', ';', '<', ',', '>', '.', '?', '/']
        
        if include == 0:
            stashArray = alphabetIsSmall + alphabetIsBig
        elif include == 1:
            stashArray = alphabetIsSmall + alphabetIsBig + numbersArray + symbolsArray

        # Create collection to store the characters
        pwdArray = []
        
        # For each iteration we create a random number and use it to fetch the index value from alphabets array. 
        for char in range(0, pwdlen):
            getChar = random.randint(0,len(stashArray) - 1)
            pwdArray.append(stashArray[getChar])

        return "".join(pwdArray)
    
    else:
        return 0
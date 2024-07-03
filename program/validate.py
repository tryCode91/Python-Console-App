def validateString(testme):
    errorcode = 0
    if isinstance(testme, str) == True:
        if len(testme) > 50:        
            errorcode = 1 
    else:
         errorcode = 2
    return errorcode

def validateInteger(number):
    errorcode = 0
    try:
        int(number)
        if(int(number) > 120):
            errorcode = 1
    except:
        errorcode = 2
    
    return errorcode
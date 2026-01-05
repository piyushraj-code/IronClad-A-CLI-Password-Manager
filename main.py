import string as st

print("This is a simple CLI based password generator")

def askPassLen():
    pass_len = int(input("Enter length of your password: "))
    return pass_len

def isSpecialChar():
    while(True):
        isSpecial = input("Do you want special characters(!@#_) in your password(y/n): ")
        if isSpecial == 'y' or 'Y':
            return True
        elif isSpecial == 'n' or 'N':
            return False
        else:
            print("Enter y/n")

def generatePassword():
    password = ""
    letters = st.ascii_letters
    digits = st.digits
    special_char = "!@#_"
    characters = ""
    passLen = askPassLen()
    isSpecial = isSpecialChar()
    if isSpecial:
        characters = letters + digits + special_char 
    else:
        characters = letters + digits
    




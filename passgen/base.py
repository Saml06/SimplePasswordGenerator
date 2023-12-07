import string
import random

special_char = "+*()+-/*="

def InjectSpecialChar(passstr):
    strlen = len(passstr)
    for i in range(1, int(strlen/4)):
        #max special characters
        randomindex = random.randint(1,strlen) - 1 #index fix
        # converting the string into list
        listed_string = list(passstr)

        # replacing the character at index with the new character
        listed_string[randomindex] = special_char[random.randint(0, len(special_char)-1)]

        # converting the list into a string again and printing it
        passstr = "".join(listed_string)

    print(passstr)

class Base():
    
    def CreateString(length):
        baseStr = ""
        for i in range(0, length):
            char = random.choice(string.ascii_letters)
            # add to string
            baseStr += char
        #add unique characters
        baseStr = InjectSpecialChar(baseStr)

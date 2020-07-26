#import random
#import math
while 1:

    mode=input("\n"+"What you want to do? Encrypt or decrypt? ")
    result=''
    modifier=0
    space_number=0
    i=0
    read_index=0
    message=''

    def getresult(a):
        if ord(a) >= 123:
            a = chr(ord(a) - 26)
        elif ord(a) <=96:
            a = chr(ord(a) + 26)
        return a

    if "decrypt" in mode.lower():

        key = input("Please enter your key: ")
        message = (input("Show me the encrypted message please: ").lower())
        message = message.rstrip().lstrip().replace(" ", "").replace("!", "").replace("?", "").replace(",", "").replace(",","")

        for i in range(len(message)):
            result += str(getresult(chr(ord(message[i].lower())-(ord(key[i-modifier].lower())-97))))

            if (i+1)%len(key)==0:
                modifier+=len(key)

            i+=1

        print("\n"+"\033[0;31;00m"+result+"\033[0m")

    elif "encrypt" in mode.lower():
    #if "encrypt" in mode.lower():

        key = input("Please enter your key: ")
        message = (input("Show me the message please: ").lower())
        message = message.rstrip().lstrip().replace(" ", "").replace("!", "").replace("?", "").replace(",", "").replace(
            ".", "")

        for i in range(len(message)):
    #if message[i]==' ':
    #    result+=''
    #else:
    #    result+=str(getresult(chr((ord(message[i])-97)+ord(key[i-modifier])))).upper()
            result += str(getresult(chr((ord(message[i]) - 97) + ord(key[i - modifier])))).upper()

            if (i+1)%len(key)==0:
                modifier+=len(key)

            i+=1

        print("\n"+"\033[0;31;00m"+result+"\033[0m")

    else:
        print("Sorry, what did you just say?" or "Sorry, I can't understand...")
        continue

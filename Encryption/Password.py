import random
import math
mode=input("What you want to do? Encrypt or decrypt? ")
key=input("Please enter your key: ")
message=(input("Show me the message please: ").lower())
result=''
modifier=0

def getresult(a):
    if ord(a)>122:
        a=chr(ord(a)-26)
    return a

for i in range(len(message)):
    result+=str(getresult(chr((ord(message[i])-97)+ord(key[i-modifier])))).upper()
    if (i+1)%len(key)==0:
        modifier+=len(key)
print(result)

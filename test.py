import socket
from datetime import datetime
from member import memberDict
import time

#TODO fix msg + crypted msg mixing tgt
#add time and condition on date match to send to specific ip for each member
dt = datetime.today().strftime('%d/%m')
s= 4
def encryp(MESSAGE, s):
    encryptedMsg = ""
   # transverse the plain text
    for i in range(len(MESSAGE)):
        char = MESSAGE[i]
        
        print(char)
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            encryptedMsg += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            encryptedMsg += chr((ord(char) + s - 97) % 26 + 97)
        return encryptedMsg

encryp("asdfghjkl", s)
#this will run the code repeatedly with fixed time
starttime = time.time()
while True:
#for every key in memberDict
#it will check if theres birthday match
#if yes it will match back the key to extract the ip address of the person
    for key in memberDict:
        if memberDict[key][0] == dt:
            UDP_IP = memberDict[key][1]
            UDP_IP = bytes.decode(UDP_IP) #change binary to string
            MESSAGE = "Happy birthday to you! " + key
            MESSAGE = str.encode(MESSAGE) #change string to binary
            UDP_PORT = 1001
            
            sock = socket.socket(socket.AF_INET, # Internet socket
                                socket.SOCK_DGRAM) # UDP
            encryp(MESSAGE, s)
            print(encryp(MESSAGE, s))
        else:
            pass
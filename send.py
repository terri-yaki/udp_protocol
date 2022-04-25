import os
import socket
from datetime import date

#TODO
#add time and condition on date match to send to specific ip for each member
#if member.dob.month && member.dob.day == datetime.datetime.now()


UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Happy birthday to you!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
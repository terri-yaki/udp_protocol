import datetime

#Create a class of member storing information from each member including name date of birth and ip address (will be using local ip)
class member :
    def __init__(member, name, dob, ip):
        member.name = name
        member.dob = dob
        member.ip = ip

john = member("john", datetime.datetime(1989, 10, 20), "192.168.0.1")

print(john.name)
print("Birthday = "+str(john.dob.day)+"/"+str(john.dob.month))
print(john.ip)
import firebase_admin
from firebase_admin import credentials, db
import datetime

cred = credentials.Certificate("../credentials/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://nest-controller.firebaseio.com/'
})

def getHour():
    return int(str(datetime.datetime.time(datetime.datetime.now())).split(":")[0])

def check(num):
    return getHour() == num and curHour != num

def setTemp(temp):
    db.reference('SetTemp').set(temp)
    print "Set Temperature to "+str(temp)+" Degrees\n"
    print "Running . . ."

curHour = -1

print "\nThis Script will set the temperature to 80 at 1AM and 77 at 9AM"
print "Use Ctrl C to stop the script\n\n"
print "Running . . ."

while True:
    try:
        if check(1):
            setTemp(80)
        elif check(9):
            setTemp(77)
        elif check(4):
            setTemp(80)
        curHour = getHour()
    except KeyboardInterrupt:
        print "\n\nScript stopped"
        print "Goodbye"
        break

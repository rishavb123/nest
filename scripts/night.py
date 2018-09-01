import firebase_admin
from firebase_admin import credentials, db
import datetime

cred = credentials.Certificate("../credentials/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://nest-controller.firebaseio.com/'
})

def getHour():
    return int(str(datetime.datetime.time(datetime.datetime.now())).split(":")[0])

curHour = -1

print "\nThis Script will set the temperature to 80 at 1AM and 77 at 9AM"
print "Use Ctrl C to stop the script\n\n"
print "Running . . ."

while True:
    try:
        if getHour() == 1 and curHour != 1:
            db.reference('SetTemp').set(80)
            print "Set Temperature to 80 Degrees\n"
            print "Running . . ."
        elif getHour() == 9 and curHour != 9:
            db.reference('SetTemp').set(77)
            print "Set Temperature to 80 Degrees\n"
            print "Running . . ."
        curHour = getHour()
    except KeyboardInterrupt:
        print "\n\nScript stopped"
        print "Goodbye"
        break

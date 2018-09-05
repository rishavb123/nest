import firebase_admin
from firebase_admin import credentials, db
import datetime

cred = credentials.Certificate("../credentials/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://nest-controller.firebaseio.com/'
})


def get_hour():
    return int(str(datetime.datetime.time(datetime.datetime.now())).split(":")[0])


def check(num):
    return get_hour() == num and curHour != num


def set_temp(temp):
    print "Set Temperature to "+str(temp)+" Degrees\n"
    print "Running . . ."
    db.reference('SetTemp').set(temp)


curHour = -1

print "\nThis Script will set the temperature to 80 at 1AM and 77 at 9AM"
print "Use Ctrl C to stop the script\n\n"
print "Running . . ."

while True:
    try:
        if check(1):
            set_temp(80)
        elif check(8):
            set_temp(77)
        curHour = get_hour()
    except KeyboardInterrupt:
        print "\n\nScript stopped"
        print "Goodbye"
        break

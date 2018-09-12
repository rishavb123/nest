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
    return hour == num and curHour != num


def set_temp(temp):
    print("Set Temperature to "+str(temp)+" Degrees\n")
    print("Running . . .")
    db.reference('SetTemp').set(temp)


curHour = -1
hour = 0

print("\nThis Script will set the temperature to a specified schedule")
print("Use Ctrl C to stop the script\n\n")
print("Running . . .")

while True:
    try:

        hour = get_hour()

        if check(1):
            set_temp(77)
        elif check(7):
            set_temp(80)
        elif check(2);
            set_temp(77)

        curHour = hour

    except KeyboardInterrupt:
        print("\n\nScript stopped")
        print("Goodbye")
        break

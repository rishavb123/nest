import firebase_admin
from firebase_admin import credentials, db
import datetime

cred = credentials.Certificate("../credentials/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://nest-controller.firebaseio.com/'
})


def get_hour():
    return int(str(datetime.datetime.time(datetime.datetime.now())).split(":")[0])


# def get_hour():
#     h = int(str(db.reference('TestHour').get()))
#     print h
#     return h


def check(num, cur_hour):
    return cur_hour == num and curHour != num


def set_temp(temp):
    print "Set Temperature to "+str(temp)+" Degrees\n"
    print "Running . . ."
    db.reference('SetTemp').set(temp)


curHour = -1

print("\nThis Script will set the temperature to a specified schedule")
print("Use Ctrl C to stop the script\n\n")
print("Running . . .")

while True:
    try:

        hour = get_hour()

        if check(1, hour):
            set_temp(80)
        elif check(6, hour):
            set_temp(77)
        elif check(8, hour):
            set_temp(83)
        elif check(19, hour):
            set_temp(80)
        elif check(20, hour):
            set_temp(77)
        curHour = hour

    except KeyboardInterrupt:
        print("\n\nScript stopped")
        print("Goodbye")
        break

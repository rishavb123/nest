import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("../credentials/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://nest-controller.firebaseio.com/'
})


def set_temp(temp):
    if not temp:
        return None
    print("Set Temperature to "+str(temp)+" Degrees\n")
    print("Running . . .")
    db.reference('SetTemp').set(temp)


def get_temp(display=False):
    temp = db.reference('CurrentTemp').get()
    if display:
        print("The Current Temperature is "+str(temp))
    return temp


def get_set_temp(display=False):
    temp = db.reference('SetTemp').get()
    if display:
        print("The Current Set Temperature is "+str(temp))
    return int(temp)


def init(use):
    print("\nThis Script will {}".format(use))
    print("Use Ctrl C to stop the script\n\n")
    print("Running . . .")


def finish():
    print("\n\nScript stopped")
    print("Goodbye")

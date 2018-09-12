import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("../credentials/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://nest-controller.firebaseio.com/'
})


def set_temp(temp):
    print("Set Temperature to "+str(temp)+" Degrees\n")
    print("Running . . .")
    db.reference('SetTemp').set(temp)


def get_temp():
    temp = db.reference('CurrentTemp').get()
    print("The Current Temperature is "+str(temp))
    return temp



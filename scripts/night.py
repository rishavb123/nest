import firebase_admin
from firebase_admin import credentials, db
import datetime

cred = credentials.Certificate("../credentials/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def getHour():
    return int(str(datetime.datetime.time(datetime.datetime.now())).split(":")[0])

curHour = -1

while True:
    if getHour() == 1 and curHour != 1:
        db.reference('SetTemp').set(80)
    elif getHour() == 9 and curHour != 9:
        db.reference('SetTemp').set(77)

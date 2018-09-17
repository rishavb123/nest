import datetime
from thermostat import set_temp, init, finish


def get_hour():
    return int(str(datetime.datetime.time(datetime.datetime.now())).split(":")[0])


def check(num):
    return hour == num and curHour != num


curHour = -1
hour = 0

init("set the temperature to a specified schedule")

while True:
    try:

        hour = get_hour()

        if check(1):
            set_temp(79)
        elif check(6):
            set_temp(77)
        elif check(8):
            set_temp(81)
        elif check(14):
            set_temp(77)

        curHour = hour

    except KeyboardInterrupt:
        finish()
        break

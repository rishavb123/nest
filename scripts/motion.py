import argparse
import cv2
import datetime
from thermostat import set_temp, init, get_set_temp, finish

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", default=0, help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=1200, help="minimum area size")
ap.add_argument("-w", "--screen-width", type=int, default=800, help="screen width")
ap.add_argument("-d", "--display", type=bool, default=False, help="Whether or not to show the display")
ap.add_argument("-t", "--time", type=bool, default=True, help="Time without motion needed to increase the temperature")

args = vars(ap.parse_args())

cam = cv2.VideoCapture(args["video"])

background = None
occupied = False

unoccupied_counter = 0
counter = 0

init("will set the temperature to 80 when there is no motion infront of the camera")

try:
    while True:

        frame = cam.read()[1]
        text = "Unoccupied"

        occupied = False

        if frame is None:
            cam = cv2.VideoCapture(args["video"])
            continue

        height, width = frame.shape[:2]
        frame = cv2.resize(frame, (args["screen_width"], int(float(args["screen_width"])/width*height)))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if background is None:
            background = gray

        frameDelta = cv2.absdiff(background, gray)
        thresh = cv2.threshold(frameDelta, 50, 255, cv2.THRESH_BINARY)[1]

        thresh = cv2.dilate(thresh, None, iterations=2)

        _, cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in cnts:
            if cv2.contourArea(c) < args["min_area"]:
                continue
            (x, y, w, h) = cv2.boundingRect(c)
            if x == 0 and y == 0 and w == args["screen_width"]:
                continue
            if args["display"]:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            text = "Occupied"
            occupied = True

        if args["display"]:
            cv2.putText(frame, "Room Status: {}".format(text), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
            cv2.imshow("Security Feed", frame)

        key = cv2.waitKey(1) & 0xFF

        if not occupied:
            unoccupied_counter += 1

        if occupied:
            unoccupied_counter = 0
            if get_set_temp() == 81:
                set_temp(77)

        if unoccupied_counter > 1000 and get_set_temp() < 81:
            set_temp(81)

        counter += 1

        if counter > 1000:
            background = None
            counter = 0

        if key == ord("q"):
            break
except KeyboardInterrupt:
    finish()

cam.release()
cv2.destroyAllWindows()


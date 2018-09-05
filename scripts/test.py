import cv2
import datetime

img1 = cv2.imread("test-photos/background1.jpg")
img2 = cv2.imread("test-photos/background3.jpg")
img3 = img2.copy()

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img1 = cv2.GaussianBlur(img1, (21, 21), 0)

img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img2 = cv2.GaussianBlur(img2, (21, 21), 0)

img = cv2.absdiff(img1, img2)
img = cv2.threshold(img, 25, 255, cv2.THRESH_BINARY)[1]

img2 = img3

img = cv2.dilate(img, None, iterations=2)

_, cnts, _ = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

text = "Unoccupied"

for c in cnts:
    if cv2.contourArea(c) < 500:
        continue
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    text = "Occupied"

cv2.putText(img2, "Room Status: {}".format(text), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
cv2.putText(img2, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, img1.shape[0] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

cv2.imshow("show", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

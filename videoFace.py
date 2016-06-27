import cv2
import sys
import Tkinter as tk

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
x_m = None
y_m = None
w_m = None
h_m = None

def keypress(event):
    if event.keysym == 'Escape':
        root.destroy()
    x = event.char
    if x == "w":
        print "blaw blaw blaw"
    elif x == "a":
        print "blaha blaha blaha"
    elif x == "s":
        print "blash blash blash"
    elif x == "d":
        print "blad blad blad"
    else:
        print x


root = tk.Tk()
root.bind_all('<Key>', keypress)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        x_m = x
        y_m = y
        w_m = w
        h_m = h
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)
    if cv2.waitKey(1)  != -1:
        crop_img = frame[y_m:y_m+h_m, x_m:x_m+w_m]
        cv2.imwrite('picturee2.jpg',crop_img)
        break



# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

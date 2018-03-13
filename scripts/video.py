# USAGE
# python3 video.py

import numpy as np
import cv2

habit_cascade = cv2.CascadeClassifier('miccal-cascades-30stages.xml')

cap = cv2.VideoCapture('miccal_uav.mp4')

while(cap.isOpened()):

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    habit = habit_cascade.detectMultiScale(frame, 1.01, 0)

    for (x,y,w,h) in habit:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),0)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    cv2.imshow('AutoMagic Invasive Plant Detector', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

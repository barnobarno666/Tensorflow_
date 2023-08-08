import cv2
import numpy as np
import requests
import urllib

url = 'http://192.168.137.227:8080/video'  # Change this to your video stream URL
cap = cv2.VideoCapture(url)
while(True):
    ret, frame = cap.read()
    if frame is not None:
        cv2.imshow('frame',frame)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break
cv2.destroyAllWindows()

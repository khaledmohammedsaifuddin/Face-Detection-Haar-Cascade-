import numpy as np
import cv2
face_c = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
#we may create our own classifier but here I have used trained classifier from OpenCv
vdo = cv2.VideoCapture(0)# capturing video and 0 index indicates my first camera
vdo.set(3,640) # set Width
vdo.set(4,480) # set Height
while True:
    retu, img_flim = vdo.read()#it's return boolean true and false  
    mg_flim = cv2.flip(img_flim, -1) # if u want to flip
    gray = cv2.cvtColor(img_flim, cv2.COLOR_BGR2GRAY)
    faces = face_c.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    for (x,y,w,h) in faces:     # (x,y) coordinate of the left upper position to draw the rectangle 
        cv2.rectangle(img_flim,(x,y),(x+w,y+h),(255,0,0),2) # draw a rectangle indicating face
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img_flim[y:y+h, x:x+w]  
    cv2.imshow('video',img_flim)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
vdo.release()
cv2.destroyAllWindows()

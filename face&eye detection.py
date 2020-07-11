import cv2
import numpy

face=cv2.CascadeClassifier(r"C:\Users\jai ganesh\Desktop\opencv\Haarcascades\haarcascade_frontalface_default.xml")

eye=cv2.CascadeClassifier(r"C:\Users\jai ganesh\Desktop\opencv\Haarcascades\haarcascade_eye.xml")

img=cv2.imread(r"C:\Users\jai ganesh\Desktop\opencv\2016-10-16-22-06-12-286.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face.detectMultiScale(gray,1.3,5)

if faces is():
    print("No faces Found")

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(127,0,255),2)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes=eye.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)
        cv2.imshow('img',img)
        cv2.waitKey(0)
    
cv2.destroyAllWindows()


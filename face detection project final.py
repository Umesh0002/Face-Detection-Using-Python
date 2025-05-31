import cv2


face_Cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#img = cv2.imread('image.jpg')
cap = cv2.VideoCapture(0)

while True:

  success,img= cap.read() 

  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

  cv2.imshow("gray image",gray)

  faces = face_Cascade.detectMultiScale(gray,1.1,4)



  for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

  cv2.imshow("Output image", img)



  k=cv2.waitKey(1)
  if k==13:
      break

cap.release()
cv2.destroyAllWindows()

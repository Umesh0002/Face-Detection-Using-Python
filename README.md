# Face-Detection-Using-Python
Output will like this
![Screenshot (72)](https://github.com/user-attachments/assets/f1accfd0-121b-4492-8be1-d2136b0b08e1)

This project is a simple Python application that performs real-time face detection using your computer's webcam. It utilizes the OpenCV library and pre-trained Haar Cascade classifiers to identify and highlight faces in a video stream.
I run this project in python IDLE, we can also run it in vs code but i prefered it to run in IDLE because simplicity of this project. If there was need of online server or use of any python extensions or running multiple files something like that i would have choosen definitely vs code.

Firstly before running this project i am suggesting that ensure you have camera on your device, because this project will capture image from video through our camera. so it is basic requirement.

# How It Works
The script captures video from your default webcam, frame by frame. Each frame is converted to grayscale, as face detection is typically performed on grayscale images to reduce complexity. The Haar Cascade classifier is then applied to the grayscale image to find faces. If faces are detected, the script draws a blue rectangle around each face on the original color frame.

# how to install open cv
use command prompt
type: pip install opencv-python

# code breakdown
here i will breakdown or we can say note down most important codes and their working in our project.
1)import cv2: Imports the necessary OpenCV library.

2)face_Cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
this is the main syntax or code of our project due to this line of code magic of face detection happens this Loads the pre-trained Haar Cascade model for frontal face detection from OpenCV's data files.

3) cap = cv2.VideoCapture(0) : Initializes the video capture object to use the default webcam (index 0).
- 'while True:': The main loop that processes the video stream continuously.
  
4) gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) : Converts the captured color frame to grayscale.

5) cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2) : Draws a blue rectangle on the original color image (`img`) at the location of the detected face.

6) cv2.imshow(...) : Displays the processed frames in a window

7) cap.release()  & cv2.destroyAllWindows(): Releases the webcam and closes all OpenCV windows, cleaning up the resources.
  
# result
In result we can see my image which shows two windows
'gray image' Shows the video feed in grayscale.
'Output image' Shows the original video feed with blue rectangles drawn around any detected faces.

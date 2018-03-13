import os
import cv2
import numpy
import tkinter
from tkinter import Tk
from tkinter import filedialog


root = Tk()
root.withdraw()

root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select image",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)

file_path = os.path.join(root.filename)



# load the input image and convert it to grayscale
image = cv2.imread(file_path)

# load the penset detector Haar cascade, then detect penset
# in the input image
# alter variable for scaleFactor, minNeighbors, minSize
detector = cv2.CascadeClassifier('Cascades/miccal-cascades-30stages.xml')
rects = detector.detectMultiScale(image, scaleFactor=1.1,
	minNeighbors=1, minSize=(24, 24))

# loop over the penset and draw a rectangle surrounding each
for (i, (x, y, w, h)) in enumerate(rects):
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.putText(image, "Target #{}".format(i + 1), (x, y - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 255), 2)

# show the detected penset
cv2.imshow("Plant", image)
cv2.imwrite("detection.jpg", image)
cv2.waitKey(0)

'''
Aidan Housenbold
X-ray image recognition

How to train a classifier
https://learncodebygaming.com/blog/training-a-cascade-classifier

https://www.geeksforgeeks.org/detect-an-object-with-opencv-python/
The code structure below is from the tutorial above and converted for my hand image detector
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

#Get the would be trainned classifier
hand_classifier = cv2.CascadeClassifier('handCascade/hand_cascade.XML')

#get the test instance you want to classify
instance = cv2.imread("1.2.826.0.1.3680043.8.498.21206216606416563283367654584074249600-c.png")

#Covert the image to gray scale for the model
gray_scaled_hand = cv2.cvtColor(instance, cv2.COLOR_BGR2GRAY)
rbg_scaled_hand = cv2.cvtColor(instance, cv2.COLOR_BGR2RGB)
#give image to the model to check
detected = hand_classifier.detectMultiScale(gray_scaled_hand,
                                   minSize =(20, 20))

# Don't do anything if there's
# no sign
detected_items = len(detected)

if detected_items != 0:

    # There may be more than one
    # sign in the image
    for (x, y, width, height) in detected:
        # We draw a green rectangle around
        # every recognized sign
        cv2.rectangle(rbg_scaled_hand, (x, y),
                      (x + height, y + width),
                      (0, 255, 0), 5)

# Creates the environment of
# the picture and shows it
plt.subplot(1, 1, 1)
plt.imshow(rbg_scaled_hand)
plt.show()
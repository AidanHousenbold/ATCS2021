'''
Aidan Housenbold
X-ray image recognition

refernce:
https://www.quora.com/How-can-I-read-a-DICOM-image-in-Python

'''

import cv2
import pydicom


ds = pydicom.dcmread('assets/archive/test/test/test/5/1.2.826.0.1.3680043.8.498.12506063821850171756494207689001728484
                     '1.2.826.0.1.3680043.8.498.72533800876543798738969965510832915095-c.dcm')



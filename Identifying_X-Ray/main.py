'''
Aidan Housenbold
X-ray image recognition

refernce:

#Help for using tensorflow for my AI
https://www.tensorflow.org/tutorials/images/classification

Help for converting images from DICOM to PNG
https://www.kaggle.com/code/ibombonato/x-ray-body-part-classification-fastai-starter

'''

import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds
import pandas as pd

#Load the data and organize it
labels = pd.read_csv('data/train_df.csv')
instances = labels[['SOPInstanceUID','Target']]

abdomen = []
ankle = []
cervicalSpine = []
chest = []
clavicles = []
elbow = []
feet = []
finger = []
forearm = []
hand = []
hip = []
knee = []
lowerLeg = []
lumbarSpine = []
others = []
pelvis = []
shoulder = []
sinus = []
skull = []
thigh = []
thoracicSpine = []
wrist = []

for UID in instances['SOPInstanceUID']:






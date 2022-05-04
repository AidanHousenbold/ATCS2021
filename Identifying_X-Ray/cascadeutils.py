'''
https://learncodebygaming.com/blog/training-a-cascade-classifier
'''
import os

def generate_negative_description_file():
    # open the output file for writing. will overwrite all existing data in there
    with open('hand_neg.txt', 'w') as f:
        # loop over all the filenames
        for filename in os.listdir('data/images/train/hand/negative'):
            f.write('data/images/train/hand/negative/' + filename + '\n')

#generate_negative_description_file()
'''
This program was used to organize files for training
'''
import os
import pandas as pd

def generate_negative_description_file():
    # open the output file for writing. will overwrite all existing data in there
    with open('hand_neg.txt', 'w') as f:
        # loop over all the filenames
        for filename in os.listdir('data/images/train/hand/negative'):
            f.write('data/images/train/hand/negative/' + filename + '\n')

'''
This function took in all of the images and created txt files with the paths
to each image so I could then use the command line

to move each photos into the correct location for positive or negative training 
'''
def create_part_textFiles():
    # load the data
    labels = pd.read_csv('data/train_df.csv')

    # add '-c.png to labels
    for path in range(0, len(labels['SOPInstanceUID'].values)):
        labels.at[path, 'SOPInstanceUID'] = labels.at[path, 'SOPInstanceUID'] + '-c.png'

    filePaths = labels['SOPInstanceUID'].values
    print(filePaths)
    images = pd.DataFrame()
    images = labels[['SOPInstanceUID', 'Target']]

    # Add only the one target to each of its respective txt files
    for image in range(0, len(labels['Target']) - 1):
        targets = images['Target'][image]
        targets.rstrip()
        t_list = targets.split(' ')
        # if len(t_list) == 2:
        #      path = "data/txt.files/" + str(t_list[0]) + ".txt"
        #      with open(path, 'a') as f:
        #          f.write(images['SOPInstanceUID'][image])
        #          f.write('\n')

#create_part_textFiles()
#generate_negative_description_file()
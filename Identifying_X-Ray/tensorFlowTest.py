
'''
code is from the article below used it to implement my model
https://medium.datadriveninvestor.com/multi-class-image-classification-in-teachable-machine-and-its-real-time-detection-with-opencv-282a1409006f
'''
import tensorflow.keras
import numpy as np
import cv2

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)
#hand
#image = cv2.imread('1.2.826.0.1.3680043.8.498.21206216606416563283367654584074249600-c.png')
#Knee
#image = cv2.imread('data/images/test/1.2.826.0.1.3680043.8.498.10200692886734407833786683970575528183-c.png')
#chest
image = cv2.imread('data/images/test/1.2.826.0.1.3680043.8.498.51783552148696762018128633402773069315-c.png')


# Load the model
model = tensorflow.keras.models.load_model('full_machine/keras_model.h5')

# Generates a dict to store the labels(keys) and its names(values)
def gen_labels():
        labels = {}
        with open("full_machine/labels.txt", "r") as label:
            text = label.read()
            lines = text.split("\n")
            print(lines)
            for line in lines[0:-1]:
                    hold = line.split(" ", 1)
                    labels[hold[0]] = hold[1]
        return labels

"""
Create the array of the right shape to feed into the keras model
The 'length' or number of images you can put into the array is
determined by the first position in the shape tuple, in this case 1."""
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# A dict that stores the labels
labels = gen_labels()


while True:
    # Choose a suitable font
    font = cv2.FONT_HERSHEY_SIMPLEX
    frame = image

    # Draw a rectangle, in the frame
    frame = cv2.rectangle(frame, (220, 80), (530, 360), (0, 0, 255), 3)
    # Draw another rectangle in which the image to labelled is to be shown.
    frame2 = frame[80:360, 220:530]
    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    frame2 = cv2.resize(frame2, (224, 224))
    # turn the image into a numpy array
    image_array = np.asarray(frame2)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array
    pred = model.predict(data)
    result = np.argmax(pred[0])

    # Print the predicted label into the screen.
    cv2.putText(frame,  "Label : " +
                labels[str(result)], (280, 400), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Exit, when 'q' is pressed on the keyboard
    if cv2.waitKey(1) and 0xff == ord('q'):
        exit = True
        break
    # Show the frame
    cv2.imshow('Frame', frame)

image.release()
cv2.destroyAllWindows()
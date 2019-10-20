//Programed by Octavia Olivia Sumailah on Patriot Hackathon 2019
//GDIT Challenge (Option 2): Image Classification
//Loaded my sample dataset using tensor flow and keras

import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

DATADIR = "/Users/octaviao.sumailah/Document/gdit_images"
CATEGORIES = ["women", "men"]

for category in CATEGORIES:
    path = os.path.join(DATADIR, category) #path to images

    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
        plt.imshow(img_array, cmap="gray")
        plt.show()
        break
    break
    
    
IMG_SIZE =50
new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
plt.imshow(img_array, cmap='gray')
plt.show() 

training_data =[]
def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category) #path to images
        for img in os.listdir(path):
            img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
            plt.imshow(img_array, cmap="gray")
            plt.show()
            break
        break
create_training_data() 


training_data =[]
def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category) #path to images
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array), (IMG_SIZE, IMG_SIZE)
                training_data.append([new_arry, class_num])
            except Exception as e:
                pass
create_training_data()

print(len(training_data))

for sample in training_data[:10]:
    print(sample[1])
    
x = []
y = []

print(img_array)

import pickle

pickle_out = open("x.pickle", "wb")
pickle.dump(x, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()


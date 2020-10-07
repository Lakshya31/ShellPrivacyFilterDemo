#!/usr/bin/env python
# coding: utf-8

# # Image Classifier

# Creating a classifier model for images

# Author: Shreyash Gupta (Chrono-Logical)

# Requirements:
# 1. tensorflow - view documentation to install
# 2. keras - view documentation to install
# 
# (If you have ananconda installed, you can simply use anaconda navigator to install both packages)

# In[1]:


import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle
from matplotlib import pyplot as plt
import cv2
import os


# In[2]:


os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'


# Model class to create a deep CNN classifier with following functions:
# 1. normalize - to normalize input feature data
# 2. build_model - to define the model
# 3. train - to train the model
# 4. save_model - to save the model and model weights
# 5. visualize - to view metrics graphically
# 6. load_model - to load a saved model
# 7. transform_image - to resize all images to required size
# 8. test - to run classifier on particular data

# CNN Model Characteristics:
# 1. Sequential model
# 2. 3 Convolutional layers - 2D Convolution and 2D Max Pooling
# 3. 2 hidden layers - Dense
# 4. 1 output layer - Dense

# In[3]:


class KerasModel():
    def __init__(self):
        self.categories = ["Safe", "Confidential"]
        self.X = pickle.load(open(os.path.join(os.path.expanduser("~"), "ShellPrivacyFilterDemo", "data", "Image Dataset", "features.pickle"), "rb"))
        self.y = pickle.load(open(os.path.join(os.path.expanduser("~"), "ShellPrivacyFilterDemo", "data", "Image Dataset", "labels.pickle"), "rb"))
        
    def normalize(self):
        self.X = self.X/255.0
        
    def build_model(self):
        self.model = Sequential()
        
        self.model.add(Conv2D(32, (3, 3),
                       activation = "relu",
                       input_shape = self.X.shape[1:]))
        self.model.add(MaxPooling2D(pool_size = (2, 2)))
        
        self.model.add(Conv2D(64, (3, 3),
                       activation = "relu"))
        self.model.add(MaxPooling2D(pool_size = (2, 2)))
        
        self.model.add(Conv2D(64, (3, 3),
                       activation = "relu"))
        self.model.add(MaxPooling2D(pool_size = (2, 2)))
        
        self.model.add(Dropout(0.25))
        
        self.model.add(Flatten())
        
        self.model.add(Dense(128,
                       activation = "relu"))
        
        self.model.add(Dense(128,
                       activation = "relu"))
        
        self.model.add(Dense(1,
                       activation = "sigmoid"))
        
        self.model.compile(loss = "binary_crossentropy", 
                           optimizer = "adam", 
                           metrics = ["accuracy"])
        
    def train(self):
        self.history = self.model.fit(self.X, self.y, batch_size = 32, epochs = 50, validation_split = 0.1)
        
    def save_model(self):
        self.model.save(os.path.join(os.path.expanduser("~"), "ShellPrivacyFilterDemo", "backend", "models", "keras_model"))
        with open(os.path.join(os.path.expanduser(), "ShellPrivacyFilterDemo", "backend", "models", "model_history"), 'wb') as file_pi:
            pickle.dump(self.history.history, file_pi)
        
    def visualize(self):
        print(self.history.keys())
        plt.figure(1)
        plt.plot(self.history['accuracy'])
        plt.plot(self.history['val_accuracy'])
        plt.title('Model Accuracy')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Validation'], loc = 'upper left')
        
    def load_model(self):
        self.model = load_model(os.path.join(os.path.expanduser("~"), "ShellPrivacyFilterDemo", "backend", "models","keras_model"))
        self.history = pickle.load(open(os.path.join(os.path.expanduser("~"), "ShellPrivacyFilterDemo", "backend", "models","model_history"), "rb"))
        
    def transform_image(self, image_path):
        img_size = 50
        img_array = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        img_array = img_array/255.0
        new_array = cv2.resize(img_array, (img_size, img_size))
        return new_array.reshape(-1, img_size, img_size, 1)
        
    def test(self, image_path):
        image = self.transform_image(image_path)
        prediction = self.model.predict([image])
        prediction = list(prediction[0])
        return self.categories[prediction.index(max(prediction))]


#!/usr/bin/env python
# coding: utf-8

# # Image model data generator

# Generating image data for classifier

# Author: Shreyash Gupta (Chrono-Logical)

# Requirements
# 1. cv2 - install using pip install opencv-python

# In[1]:


import numpy as np
import os
from matplotlib import pyplot as plt
import cv2
import random
import pickle


# Class to generate image-label data with following functions
# 1. find_images - to read images into an array
# 2. generate_training_data - to create a list of training data
# 3. features_labels - to extract features and labels from data
# 4. save_pickle - to save data in pickle format
# 5. load_pickle - to load data from pickle file

# In[2]:


class ImageData:
    def __init__(self, categories, data_path, image_size):
        self.categories = categories
        self.data_path = data_path
        self.image_size = image_size
        
    def find_images(self):
        for category in self.categories:
            img_path = os.path.join(self.data_path, category)
            for image in os.listdir(img_path):
                img_array = cv2.imread(os.path.join(img_path, image), cv2.IMREAD_GRAYSCALE) 
            
    def generate_training_data(self):
        self.training_data = []
        for category in self.categories:
            img_path = os.path.join(self.data_path, category)
            class_num = self.categories.index(category)
            for image in os.listdir(img_path):
                try:
                    img_array = cv2.imread(os.path.join(img_path, image), cv2.IMREAD_GRAYSCALE)
                    new_array = cv2.resize(img_array, (self.image_size, self.image_size))
                    self.training_data.append([new_array, class_num])
                except Exception:
                    pass
        
        random.shuffle(self.training_data)
                
    def features_labels(self):
        self.X = []
        self.y = []
        for features, label in self.training_data:
            self.X.append(features)
            self.y.append(label)
            
        self.X = np.array(self.X).reshape(-1, self.image_size, self.image_size, 1)
        self.y = np.array(self.y)
        
    def save_pickle(self):
        pickle_out = open(os.path.join(os.path.expanduser("~"), "data", "Image Dataset", "features.pickle"), "wb")
        pickle.dump(self.X, pickle_out)
        pickle_out.close()

        pickle_out = open(os.path.join(os.path.expanduser("~"), "data", "Image Dataset", "labels.pickle"), "wb")
        pickle.dump(self.y, pickle_out)
        pickle_out.close()
        
    def load_pickle(self):
        pickle_in = open(os.path.join(os.path.expanduser("~"), "data", "Image Dataset", "features.pickle"), "rb")
        self.X = pickle.load(pickle_in)


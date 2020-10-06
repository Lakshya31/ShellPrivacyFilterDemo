#!/usr/bin/env python
# coding: utf-8

# # Image Classifier

# Creating a classifier model for images

# Author: Shreyash Gupta (Chrono-Logical)

# In[ ]:


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle
from keras.models import model_from_json
from keras.models import load_model
from matplotlib import pyplot as plt


# In[ ]:


class KerasModel():
    def __init__(self):
        self.X = pickle.load(open("features.pickle", "rb"))
        self.y = pickle.load(open("labels.pickle", "rb"))
        
    def normalize(self):
        self.X = self.X/255.0
        
    def build_model(self):
        self.model = Sequential()
        
        self.model.add(Conv2D(16, 3, 3),
                       activation = "relu",
                       input_shape = X.shape[1:])
        self.model.add(MaxPooling2D(pool_size = (2, 2)))
        
        self.model.add(Conv2D(32, 3, 3),
                       activation = "relu")
        self.model.add(MaxPooling2D(pool_size = (2, 2)))
        
        self.model.add(Conv2D(64, 3, 3),
                       activation = "relu")
        self.model.add(MaxPooling2D(pool_size = (2, 2)))
        
        self.model.add(Conv2D(64, 3, 3),
                       activation = "relu")
        self.model.add(MaxPooling2D(pool_size = (2, 2)))
        
        self.model.add(Conv2D(64, 3, 3),
                       activation = "relu")
        self.model.add(MaxPooling2D(pool_size = (2, 2)))
        
        self.model.add(Flatten())
        
        self.model.add(Dense(512),
                       activation = "relu")
        
        self.model.add(Dense(1),
                       activation = "sigmoid")
        
        self.model.compile(loss = "binary_crossentropy", 
                           optimizer = "adam", 
                           metrics = ["accuracy"])
        
    def train(self):
        self.history = self.model.fit(X, y, batch_size = 32, epochs = 50, validation_split = 0.1)
        
    def save_model(self):
        model_json = self.model.to_json()
        with open("keras_model.json", "w") as json_file:
            json_file.write(model_json)
            
        self.model.save_weights("keras_model.h5")
        
        self.model.save("keras_model")
        
    def visualize(self):
        print(self.history.history.keys())
        plt.figure(1)
        plt.plot(self.history.history['acc'])
        plt.plot(self.history.history['val_acc'])
        plt.title('Model Accuracy')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Validation'], loc = 'upper left')
        
    def load_model(self):
        self.model = load_model("keras_model")
        
    def transform_image(self, image_path):
        img_size = 50
        img_array = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        new_array = cv2.resize(img_array, (img_size, img_size))
        return new_array.reshape(-1, img_size, img_size, 1)
        
    def test(self, image_path):
        image = self.transform_image(image_path)
        prediction = self.model.predict([image])
        prediction = list(prediction[0])
        print(self.categories[prediction.index(max(prediction))])
        return self.categories[prediction.index(max(prediction))]


# In[ ]:


model = KerasModel()


# In[ ]:


model.normalize()


# In[ ]:


model.build_model()


# In[ ]:


model.train()


# In[ ]:


model.save_model()


# In[ ]:


model.visualize()


# In[ ]:


image = "path"


# In[ ]:


model.test(image)


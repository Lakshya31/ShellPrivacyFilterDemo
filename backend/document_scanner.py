#!/usr/bin/env python
# coding: utf-8

# # Document scanner

# Reading docx files for text and images that may be confidential.

# Author: Shreyash Gupta (Chrono-Logical)

# Requirements
# 1. docx - install using pip install python-docx

# In[1]:


import docx
import zipfile
import os
import shutil


# Class for extracting from document file with following functions
# 1. extract_text - to extract all the text information from file.
# 2. extract_images - to extract all the images in document.

# In[2]:


class DocumentExtract:
    def __init__(self):
        self.images = []
    
    def extract_text(self, input_file, output_text):
        doc = docx.Document(input_file)
        with open(input_file.split("/")[-1].split(".")[0] + "_" + output_text + ".txt", "w",encoding = "utf-8") as file:
            for para in doc.paragraphs:
                file.write(para.text + u"\n")
    
    def extract_images(self, input_file, output_img):
        with zipfile.ZipFile(input_file) as doc:
            for info in doc.infolist():
                if info.filename.endswith((".png", ".jpeg", ".gif")):
                    doc.extract(info.filename, output_img)
                    shutil.copy(output_img + "/" + info.filename, 
                                output_img + "/" + input_file.split("/")[-1].split(".")[0] + "_" + info.filename.split("/")[-1])
                    self.images.append(input_file.split("/")[-1].split(".")[0] + "_" + info.filename.split("/")[-1])


# Creating instance of class

# In[3]:


document = DocumentExtract()


# Defining input parameters

# In[4]:


input_file = "abc.docx"
output_text = "text"
output_img = "images"


# Extracting text and images

# In[5]:


document.extract_text(input_file, output_text)
document.extract_images(input_file, output_img)


#!/usr/bin/env python
# coding: utf-8

# # HSSE Email Filter

# Filtering e-mail content for potentially confidential data.

# Author: Shreyash Gupta (Chrono-Logical)

# In[1]:


from spacy_ner import NER
from document_scanner import DocumentExtract
from keras_model import KerasModel
import os


# In[2]:


os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'


# Class to implement all filtering functions on email with following functions:
# 1. load_ner - load NER model
# 2. load_image_model - to load image classifier
# 3. email_ner - to run NER on email text
# 4. attachment_ner - to run NER on text in attachment
# 5. attachment_image - to run image classification on images in attachment
# 6. attachment_scan - to scan attachment content for unsafe information
# 7. return_results - to return all results

# In[3]:


class EmailFilter:
    def __init__(self):
        self.load_ner()
        self.load_image_model()
         
    def load_ner(self):
        self.ner = NER()
        self.ner.load(os.path.join(os.path.expanduser("~"),"ShellPrivacyFilterDemo","backend", "models", "ner_model"))
        
    def load_image_model(self):
        self.keras_model = KerasModel()
        self.keras_model.load_model()
        
    def email_ner(self, text):
        return self.ner.test(text)
    
    def attachment_ner(self, attachment_docx):
        self.de.extract_text(attachment_docx, "text")
        with open(os.path.join(os.path.expanduser("~"), "ShellPrivacyFilterDemo", "data", attachment_docx.split(".")[0] + "_text.txt"), "r") as file:
            text = file.read()
            ner_result = self.ner.test(text)
            
            if len(ner_result) > 0:
                return True
        
        return False
    
    def attachment_image(self, attachment_docx):
        self.de.extract_images(attachment_docx, "images")
        predictions = []
        for image in self.de.images:
            predictions.append(self.keras_model.test(os.path.join(os.path.expanduser("~"), "ShellPrivacyFilterDemo", "data", "images", image)))
        
        if "Confidential" in predictions:
            return True
        
        return False
    
    def attachment_scan(self, attachment_docx):
        self.de = DocumentExtract()
        unsafe_text = self.attachment_ner(attachment_docx)
        unsafe_image = self.attachment_image(attachment_docx)
        
        if unsafe_text == True or unsafe_image == True:
            return "issue"
        
        return "no issue"


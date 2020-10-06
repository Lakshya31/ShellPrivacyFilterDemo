#!/usr/bin/env python
# coding: utf-8

# # HSSE Email Filter

# Filtering e-mail content for potentially confidential data.

# Author: Shreyash Gupta (Chrono-Logical)

# In[ ]:


from spacy_ner import NER
from document_scanner import DocumentExtract
from keras_model import KerasModel


# In[ ]:


class EmailFilter:
    def __init__(self, email_text, attachment_docx):
        self.load_ner()
        self.load_image_model
         
    def load_ner(self):
        self.ner = NER()
        self.ner.load("ner_model")
        
    def load_image_model(self):
        self.keras_model = KerasModel()
        self.keras_model.load_model()
        
    def email_ner(self, text):
        return self.ner.test(text)
    
    def attachment_ner(self, attachment_docx):
        self.de.extract_text(attachment_docx)
        with open(attachment_docx + "_text.txt", "r") as file:
            text = file.read()
            personal, confidential = self.ner.test(text)
            
            if len(personal > 0) or len(confidential) > 0:
                return True
        
        return False
    
    def attachment_image(self, attachment_docx):
        self.de.extract_images(attachment_docx, "images")
        predictions = []
        for image in self.de.images:
            predictions.append(self.keras_model.test("images/" + image))
        
        if "Confidential" in predictions:
            return True
        
        return False
    
    def attachment_scan(self, attachment_docx):
        self.de = DocumentExtract()
        unsafe_text = self.attachment_ner(attachment_docx)
        unsafe_image = self.attachment_image(attachment_docx)
        
        if unsafe_text == True or unsafe_image == True:
            return True
        
        return False
    
    def return_results(self):
        e_ner_personal, e_ner_confidential = self.email_ner(email_text)
        unsafe = self.attachment_scan(attachment_docx)
        
        return e_ner_personal, e_ner_confidential, unsafe


# In[ ]:


hsse_filter = EmailFilter(text_extracted_from_email, attachment_from_email)
ep, ec, unsafe = hsse_filter.return_results()


#!/usr/bin/env python
# coding: utf-8

# # Named Entity Recognition using spaCy NER

# Recogizing personal, official, confidential entities from text using custom NER model built using spaCy.

# Author: Shreyash Gupta (Chrono-Logical)

# Requirements
# 1. spacy - use pip install spacy

# In[ ]:


import spacy
import random
import json
import re


# NER class with following functions
# 1. jsonl_to_spacy - converts Doccano annotated file (jsonl) to suitable form for spaCy NER training
# 2. clean_entity_spans - to fix entity spans for NER
# 3. train_spacy - used to train the NER model using the generated train data over given number of iterations.
# 4. save_model - saves the model with the given name, for given data and number of iterations.
# 5. test - tests the model for specific input text

# In[ ]:


class NER:
    def jsonl_to_spacy(self, input_file):
        with open(input_file, 'rb') as file:
            data = file.readlines()
            training_data = []
            
            for line in data:
                entities = []
                record = json.loads(line)
                text = record["text"]
                ent = record["labels"]
            
                for start, end, label in ent:
                    entities.append((start, end, label))
            
                training_data.append((text, {"entities": entities}))
            
            return training_data
        
    def clean_entity_spans(self, data):
        invalid_span_tokens = re.compile(r'\s')

        cleaned_data = []
            
        for text, annotations in data:
            entities = annotations['entities']
            valid_entities = []
            
            for start, end, label in entities:
                valid_start = start
                valid_end = end
                
                while valid_start < len(text) and invalid_span_tokens.match(text[valid_start]):
                    valid_start += 1
                
                while valid_end > 1 and invalid_span_tokens.match(text[valid_end - 1]):
                    valid_end -= 1
                
                valid_entities.append([valid_start, valid_end, label])
            
            cleaned_data.append([text, {'entities': valid_entities}])

        return cleaned_data
    
    def train_spacy(self, train_data, iterations):
        TRAIN_DATA = train_data
        nlp = spacy.blank('en')
        if 'ner' not in nlp.pipe_names:
            ner = nlp.create_pipe('ner')
            nlp.add_pipe(ner, last = True)
            
        for _, annotations in TRAIN_DATA:
            for ent in annotations.get('entities'):
                ner.add_label(ent[2])
                
        other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
        with nlp.disable_pipes(*other_pipes):
            optimizer = nlp.begin_training()
            for iteration in range(iterations):
                print("Starting iteration " + str(iteration))
                random.shuffle(TRAIN_DATA)
                losses = {}
                for text, annotations in TRAIN_DATA:
                    nlp.update(
                        [text],
                        [annotations],
                        drop = 0.2,
                        sgd = optimizer,
                        losses = losses)
                print(losses)
    
        return nlp
    
    def save_model(self, path, data, iterations):
        self.ner_model = self.train_spacy(data, iterations)
        self.ner_model.to_disk(path)
        
    def test(self, text):
        doc = self.ner_model(text)
        personal = []
        confidential = []
        
        for ent in doc.ents:
            print(ent.text, ent.label_, (ent.start_char, ent.end_char))
            if ent.label_ == "Confidential":
                confidential.append((ent.start_char, ent.end_char))
            elif ent.label_ == "Personal":
                personal.append((ent.start_char, ent.end_char))
        
        return personal, confidential
            
    def load(self, path):
        self.ner_model = spacy.blank('en')
        if 'ner' not in self.ner_model.pipe_names:
            ner = self.ner_model.create_pipe('ner')
            self.ner_model.add_pipe(ner, last = True)
        self.ner_model.from_disk(path)





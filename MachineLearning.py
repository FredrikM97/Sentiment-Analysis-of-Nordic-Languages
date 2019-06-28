'''
LSTM model for sentiment prediction of reviews
'''
from __future__ import print_function
print('Importing packages...')
from sklearn.model_selection import train_test_split
import pandas as pd
from zipfile import ZipFile
from gensim.models import KeyedVectors

import os
import sys
stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential, load_model
from keras.layers import Dense, Embedding, GRU, LSTM
from keras import optimizers
sys.stderr = stderr
import matplotlib.pyplot as plt
import numpy as np

# Enviroment variables
REPOSITORY = ["D:/Exjobb/models/", "D:/Exjobb/embedding/", "D:/Exjobb/data/"]
EMBEDDINGZIP = ["69 swe.zip", "38 dan.zip", "58 nor.zip"]

# Keras model variables
MAXLEN = 250
BATCH_SIZE = 50

# Load training data
print('Loading data...')

#Excel files
swe_data = pd.io.excel.read_excel(REPOSITORY[2]+'Allt utom golf_se.xlsx', sheet_name=[4], dtype={'Comment': str})
swe_data = pd.concat([swe_data[i] for i in swe_data.keys()],ignore_index=True)

#CSV files
#df2 = pd.read_csv(REPOSITORY+'golf_se.csv',sep=';',dtype={'aw':str,'asd':float},encoding='utf_8')
#df2 = df2.rename({'aw':'Comment', 'asd':'NPS'}, axis='columns')

#swe_data = pd.concat([df1,df2],sort=False,ignore_index=True)
swe_data['NPS'] = pd.to_numeric(swe_data['NPS'], errors='coerce')
swe_data.dropna(inplace=True)
swe_data['Comment'] = swe_data['Comment'].astype(str).str.lower().str.replace(r'[^\w ]', '')

# Gensim model (embedding)
print('Loading embedding...')
with ZipFile(REPOSITORY[1] + EMBEDDINGZIP[2], "r") as archive:
  stream = archive.open("model.txt")
  embedding = KeyedVectors.load_word2vec_format(
      stream, binary=False, unicode_errors='replace')

# Preprocessing
def tokenize(sentence,word_list):
    tokens = []
    for word in sentence.split():
        try:
            tokens.append(word_list.vocab[word].index)
        except:
            tokens.append(0)
    return tokens

def preprocess(string_series):
  string_series = string_series.map(lambda s: tokenize(s,embedding))
  string_series = sequence.pad_sequences(string_series, maxlen=MAXLEN)
  return string_series

x_train, x_test, y_train, y_test = train_test_split(
    preprocess(swe_data['Comment']),
    swe_data['NPS'],
    train_size=0.7,
    test_size=0.3,
    random_state=42)
print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)

# Model
print('Building model...')
def build_model(embedding):
    keras_embedding = Embedding(
        input_dim = len(embedding.vocab),
        output_dim = embedding.vector_size,
        weights = [embedding.vectors],
        input_length=MAXLEN,
        trainable=False)

    layer1 = GRU(
        units=100,
        dropout=0.5,
        recurrent_dropout=0.5,
        return_sequences=True)

    layer2 = GRU(
        units=100,
        dropout=0.5,
        recurrent_dropout=0.5,
        return_sequences=False)

    dense_node = Dense(1, activation=None, kernel_regularizer=None)
    
    model = Sequential()
    model.add(keras_embedding)
    model.add(layer1)
    model.add(layer2)
    model.add(dense_node)
    model.compile(optimizer='rmsprop',loss='mae')
    return model
model = build_model(embedding)

# Testing
hitory = model.fit(
  x_train, y_train,
  batch_size=BATCH_SIZE,
  epochs=15,
  verbose=2,
  validation_data=(x_test, y_test))
print('Evaluate... ',)
loss = model.evaluate(x_test, y_test,batch_size=BATCH_SIZE,verbose=0)
print('Test loss:', loss)

# Usefull functions
def sentiment(sentence):
    return str(model.predict(preprocess(pd.Series(sentence)))[0][0])

def save():
    model.save(REPOSITORY[0]+'nor_model.h5')

def load():
    model = load_model(REPOSITORY+'swe_model_GRU_FRE_T1.h5')

def boxplot():
  pre = model.predict(x_test)
  data = y_test.subtract(pre[:,0])
  fig, ax = plt.subplots()
  ax.set_title('Error boxplot')
  ax.boxplot(data, vert=False)
  fig.show()
  
def histogram():
  n, bins, patches = plt.hist(swe_data.NPS,11)
  plt.xlabel('Score')
  plt.ylabel('Amount of reviews')
  plt.title('Review Distribution')
  plt.show()
  
def correlation():
  pre = model.predict(x_test)
  return np.corrcoef([y_test,pre[:,0]])

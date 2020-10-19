import numpy as np 
import pandas as pd 
import boto3 
import pickle
from pickle import dump
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense  
from keras.layers import LSTM
from keras.layers import Embedding
from keras.layers.core import Dropout, Activation
from keras.callbacks import ModelCheckpoint



def load_doc(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text

def compile_LSTM_model(nodes):
    model = Sequential()
    model.add(Embedding(vocab_size, 50, input_length=seq_length))
    model.add(LSTM(nodes, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(nodes))
    model.add(Dropout(0.2))
    model.add(Dense(nodes, activation='relu'))
    model.add(Dense(vocab_size, activation='softmax'))
    return model

def compile_LSTM_dropout_model(nodes, dropout_val):
    model = Sequential()
    model.add(Embedding(vocab_size, 50, input_length=seq_length))
    model.add(LSTM(nodes, return_sequences=True))
    model.add(Dropout(dropout_val))
    model.add(LSTM(nodes))
    model.add(Dropout(dropout_val))
    model.add(Dense(nodes, activation='relu'))
    model.add(Dense(vocab_size, activation='softmax'))
    return model




if __name__ == '__main__':
    in_filename = 'trump_sequences.txt'
    doc = load_doc(in_filename)
    lines = doc.split('\n')
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(lines)
    sequences = tokenizer.texts_to_sequences(lines)
    vocab_size = len(tokenizer.word_index) + 1
    sequences_arr = np.array(sequences)
    X, y = sequences_arr[:,:-1], sequences_arr[:, -1]
    y = to_categorical(y, num_classes=vocab_size)
    seq_length = X.shape[1]
    model = compile_LSTM_model(256)
    filepath="weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
    checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
    callbacks_list = [checkpoint]
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    # fit model
    model.fit(X, y, batch_size=300, epochs=200, callbacks=callbacks_list)
    # save the model to file
    model.save('model.h5')
    # save the tokenizer
    dump(tokenizer, open('tokenizer.pkl', 'wb'))

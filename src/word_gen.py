from pickle import load
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import random
from random import randint
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
from keras.layers import Embedding
 
# load doc into memory
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text
 
# generate a sequence from a language model
def generate_seq(model, tokenizer, seq_length, seed_text, n_words):
	result = list()
	in_text = seed_text
	# generate a fixed number of words
	for _ in range(n_words):
		# encode the text as integer
		encoded = tokenizer.texts_to_sequences([in_text])[0]
		# truncate sequences to a fixed length
		encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
		# predict probabilities for each word
		yhat = model.predict_classes(encoded, verbose=0)
		# map predicted word index to word
		out_word = ''
		for word, index in tokenizer.word_index.items():
			if index == yhat:
				out_word = word
				break
		# append to input
		in_text += ' ' + out_word
		result.append(out_word)
	return ' '.join(result)
 

if __name__ == '__main__':
    # load cleaned text sequences
    in_filename = 'trump_sequences_no_tweets.txt'
    weights_filename = "weights-improvement-11-4.9073.hdf5"
    tokenizer = load(open('tokenizer.pkl', 'rb'))
    model = load_model('model.h5')
    doc = load_doc(in_filename)
    lines = doc.split('\n')
    seq_length = len(lines[0].split()) - 1
 
    # select a seed text
    seed_text = lines[randint(0,len(lines))]
    print(seed_text + '\n')
 
    # generate new text
    generated = generate_seq(model, tokenizer, seq_length, seed_text, 50)
    print(generated)

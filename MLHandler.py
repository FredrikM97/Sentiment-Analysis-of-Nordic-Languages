from keras.models import Sequential, load_model
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
import pandas as pd
from zipfile import ZipFile
from gensim.models import KeyedVectors

MAXLEN = 250

REPOSITORY = ["D:/Exjobb/models/", "D:/Exjobb/embedding/"]
EMBEDDINGZIP = ["69 swe.zip", "38 dan.zip", "58 nor.zip"]

# Gensim model (embedding)
def loadEmbedding(language):
	print('Loading embedding...' + language)
	with ZipFile(REPOSITORY[1] + language, "r") as archive:
		stream = archive.open("model.txt")
		embedding = KeyedVectors.load_word2vec_format(
			stream, binary=False, unicode_errors='replace')
	return embedding


# Preprocessing
def tokenize(sentence,word_list):
    tokens = []
    for word in sentence.split():
        try:
            tokens.append(word_list.vocab[word].index)
        except:
            tokens.append(0)
    return tokens

# Input: String and the embedding
def preprocess(string_series, embedding):
    string_series = string_series.astype(str).str.lower().str.replace(r'[^\w ]', '')
    string_series = string_series.map(lambda s: tokenize(s,embedding))
    string_series = sequence.pad_sequences(string_series, maxlen=MAXLEN)
    return string_series

# Load existing model
def loadModel(dataModel):
    model = load_model(REPOSITORY[0]+dataModel)
    model._make_predict_function()
    return model

# Return sentiment
def sentiment(sentence, lang):
	if lang == "swe":
		return str(model_swe.predict(preprocess(pd.Series(sentence), embedding_swe))[0][0])
	elif lang == "dan": 
		return str(model_dan.predict(preprocess(pd.Series(sentence), embedding_dan))[0][0])
	elif lang == "nor":
		return str(model_nor.predict(preprocess(pd.Series(sentence), embedding_nor))[0][0])
	
embedding_swe = loadEmbedding(EMBEDDINGZIP[0]) #Swedish embedding
embedding_dan = loadEmbedding(EMBEDDINGZIP[1]) #Danish embedding
embedding_nor = loadEmbedding(EMBEDDINGZIP[2]) #Norwegian embedding


model_swe = loadModel('swe_regression_gru.h5')
model_dan = loadModel('dan_model_GRU_FRE_T1.h5') 
model_nor = loadModel('nor_model_GRU.h5')

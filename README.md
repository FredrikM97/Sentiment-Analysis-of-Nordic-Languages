# Bachelor Thesis - Sentiment Analysis of Nordic Languages

This project is a bachelor thesis in computer science at Halmstad University. The project is done by Fredrik Mårtensson and Jesper Holmblad. The project aims to investigate the possibility of extracting a tonality through sentiment analysis of the Nordic languages; Swedish, Danish and Norwegian.

The webservice can be started through Flask framework using python server.py

## Load a model

Start the MachineLearning.py file, edit layer1/layer2 and use following parameters/Settings:
#### LSTM model:
Batch_size 50
Epochs: 40
Units: 80
This will give approximatelu 65.8% correlation

#### GRU model:
Batch_size 50
Epochs: 15
Units: 100
This will give approximatelu 61.7% correlation

Modifications can be made, good hardware required. 
Check size of files in order to know how much ram that is required. 

#### Configuration
Check that right directory and files is selected, alternative if CSV or XMLX exists inside the folder.

Save the model that is created and add it to the MLHandler.py and start the webservice through server.py

## Embedding
The embedding can be found at: 
http://vectors.nlpl.eu/repository/ <br />

#### Swedish: <br />
ID: 69 <br />
Vector size: 100 <br />
Corpus: Swedish CoNLL17 corpus <br />
Algorithm: Word2Vec Continuous Skipgram <br />
Lemmatization: False <br />

#### Danish: <br /> 
ID: 38 <br />
Vector size: 100 <br />
Corpus: Danish CoNLL17 corpus <br />
Algorithm: Word2Vec Continuous Skipgram <br />
Lemmatization: False <br />

#### Norwegian: <br />
ID: 58 <br />
Vector size: 100 <br />
Corpus: Norwegian-Bokmaal CoNLL17 corpus <br />
Algorithm: Word2Vec Continuous Skipgram <br />
Lemmatization: False <br />




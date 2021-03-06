from numpy import loadtxt
from keras.models import load_model
import tensorflow as tf
import pandas as pd
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
import pickle
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.backend import set_session

global session
session = tf.Session(graph=tf.Graph())

with session.graph.as_default():
    K.set_session(session)
    loaded_model = load_model('filter_dir/model_dir/models819.h5')

global graph
graph = tf.get_default_graph()

with open('filter_dir/model_dir/tokenizer819.pickle', 'rb') as handle:
    loaded_tokenizer = pickle.load(handle)

def classify(txt):
    seq= loaded_tokenizer.texts_to_sequences([txt])
    padded = pad_sequences(seq, maxlen=42)
    with session.graph.as_default():
        K.set_session(session)
        pred = loaded_model.predict(padded)
    if round(pred[0][0])==1:
        return 1
    elif round(pred[0][1])==1:
        return -1
    elif round(pred[0][2])==1:
        return 0

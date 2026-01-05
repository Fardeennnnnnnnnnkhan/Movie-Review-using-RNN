#Step -1 Import Libraries and Load the Model
import numpy as np
import tensorflow as tf 
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence 
from tensorflow.keras.models import load_model

#load the IMDB dataset word index 
model = load_model('simplernn_imdb_model.h5')


## Mapping of word indices back to words(for understanding)
word_index = imdb.get_word_index()
reverse_word_index = {value:key for (key,value) in word_index.items()}

#Preprocess text
def preprocess_text(review):
    tokens = review.lower().split()
    encoded = [word_index.get(word, 2) + 3 for word in tokens]
    padded_sequence =sequence.pad_sequences([encoded], maxlen=500)
    return padded_sequence

#Prediction Function
def predict_sentiment(review):
    preprocessed_input  = preprocess_text(review)

    predict = model.predict(preprocessed_input)
    sentiment = "Positive" if predict[0][0] >= 0.5 else "Negative"
    return sentiment , predict[0][0] 


import streamlit as st 

st.title('IMDB Movie Review Sentiment Analysis')
st.write('Enter a movie review to classify it as positive or negative')

user_input = st.text_area('Movie Review')

if st.button('Classify'):
    preprocess_input= preprocess_text(user_input)
    
    #Make Prediction
    prediction = model.predict(preprocess_input)

    #display the result
    st.write(f'Sentiment : {sentiment}')
    score = prediction[0][0] * 100
    st.write(f'Prediction Score : {score:.1f}%')

else :
    st.write(f'Please enter a movie review')
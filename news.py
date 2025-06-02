import streamlit as st
import pickle
import spacy

with open('data.pkl','rb') as model_file:
    model = pickle.load(model_file)

nlp = spacy.load('en_core_web_lg')
st.title("News Detecatoin App")
st.write("This app detects wheather news is real or fake")

a = st.text_input('enter news')
doc = nlp(a)
vector = doc.vector
prediction = model.predict([vector])
if prediction[0] == 1:
    st.write("This is **real**.")
else:
    st.write("fake news")

# -*- coding: utf-8 -*-
"""app

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LNvZ5Ga9nnDLJXyftB30EfSec8Z0DSpI
"""

import streamlit as st
import pandas as pd
from ast import literal_eval
from cdqa.utils.converters import pdf_converter
from cdqa.pipeline import QAPipeline
from cdqa.utils.download import download_model

import urllib.request
from fpdf import FPDF
import base64

import webbrowser


download_model(model='bert-squad_1.1', dir='./models')
df = pdf_converter(directory_path="docs/FIRE AND LIFE SAFETY CODE_Page24.pdf")

print(df.head())

pd.set_option('display.max_colwidth', -1)
df.head()
cdqa_pipeline = QAPipeline(reader='./models/bert_qa.joblib', max_df=1.0)

cdqa_pipeline.fit_retriever(df=df)


n_predictions=st.sidebar.slider(label="Number Of Predictions",min_value=1,max_value=5)


#query = ' What is Fire Fighting system for above 90m building height ?'
st.title('Query Answering AI Bot')

query=st.text_input("Enter Text: ")

if query:
    prediction = cdqa_pipeline.predict(query, n_predictions=n_predictions)
    for i,value in enumerate(prediction):
        answer,title,paragraph,predictionsss=value
        answer_var=st.write("Answer: "+answer)
        title_var=title.replace(" ","%20")
        #url="https://github.com/hebaarch/docs/raw/main/"+title_var+".pdf"
        url="https://github.com/mohsinmushtaq-arch/pdf-docs/raw/main/docs/"+title_var+".pdf"
        print(url)
        
        paragraph_var=st.write("Paragraph: " + paragraph)
        #download_button = st.button(title+'_no:'+str(i))
        #download_button = st.markdown(url, unsafe_allow_html=True)
        #st.markdown("<a style='display: block; text-align: center;' href= url > Download report</a>",unsafe_allow_html=True,)
        st.markdown("Download This Report Here [link](%s)" % url)
        
        #if download_button:
            #st.markdown(url, unsafe_allow_html=True)

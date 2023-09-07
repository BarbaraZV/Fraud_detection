#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pickle
import streamlit as st
from PIL import Image
import base64
st.sidebar.title('Trnsaction Information')
from IPython import get_ipython
import pandas as pd

html_temp = """
<div style="background-color:Blue;padding:10px">
<h2 style="color:white;text-align:center;">Fraud Detection</h2>
</div><br>
"""

st.markdown(html_temp,unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: Black;'>Select Your Model</h1>", unsafe_allow_html=True)
selection = st.selectbox("",["Decision Tree","Logistic Regression", "Random Forest"])
if selection == "Decision Tree":
    st.write("You selected", selection, "model")
    model = pickle.load(open(r"C:\Users\Barbara\OneDrive\Documents\GitHub\IH_final_project\decision_tree_model_app", "rb"))
elif selection == "Logistic Regression":
    st.write("You selected", selection, "model")
    model = pickle.load(open(r"C:\Users\Barbara\OneDrive\Documents\GitHub\IH_final_project\logistic_regression_model_app", "rb"))
else:
    st.write("You selected", selection, "model")
    model = pickle.load(open(r"C:\Users\Barbara\OneDrive\Documents\GitHub\IH_final_project\random_forest_model_app", "rb"))

amt = st.sidebar.slider(label = "amt", min_value = -12.00, max_value= 18.00, step=0.01)
unix_time = st.sidebar.slider(label = "unix_time", min_value = -7.00, max_value= 6.00, step=0.01)

coll_dict = {"amt":amt,"unix_time": unix_time }
columns =["amt", "unix_time"]

df_coll=pd.DataFrame.from_dict([coll_dict])
user_inputs = df_coll
prediction = model.predict(user_inputs)
html_temp="""
<div style="background-color:Black;padding:10px">
<h2 style="color:white;text-align:center;">Fraud Detection Prediction</h2>
</div><br>
"""

st.markdown("<h1 style='text-align: center; color: Black;'>Transaction information</h1>", unsafe_allow_html=True)
st.table(df_coll)
st.subheader('Click PREDICT if configuration is OK')

if st.button('PREDICT'):
    if prediction[0]==0:
        st.success(prediction[0])
        st.success(f'Transaction is SAFE :)')
    elif prediction[0]==1:
        st.warning(prediction[0])
        st.warning(f'ALARM! TRANSACTION IS FRAUDULENT :( ')


import pandas as pd
import streamlit as st
st.title("text input")
name=st.text_input("Enter your name:")
age=st.slider("choose ypur age",1,100,25)
options=["java","python","javascript"]
choice=st.selectbox("select your fav language",options)
file_uploaded=st.file_uploader("Upload file",type=["csv","pdf","xlsx"])
if file_uploaded:
    data=pd.read_excel(file_uploaded)
    st.write(data)
if name and age and choice:
    st.write(f"hello ,{name}. your age is {age}. and you are {choice} programmer.")

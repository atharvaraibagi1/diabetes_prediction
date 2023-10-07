import pandas as pd
import numpy as np
import streamlit as st
import pickle

model = pickle.load(open("C:/Users/Atharva/Desktop/rxib/Diabetes_Prediction_Model_Practice/diabetes_prediction/diabetes_model.sav",'rb'))

st.title("Diabetes Prediction")
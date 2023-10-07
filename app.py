import pandas as pd
import numpy as np
import streamlit as st
import pickle

model = pickle.load(open("C:/Users/Atharva/Desktop/rxib/Diabetes_Prediction_Model_Practice/diabetes_prediction/diabetes_model.sav",'rb'))

def diabetes_prediction(input_data):
    input_data_reshape = np.asarray(input_data).reshape(1,-1)
    prediction = model.predict(input_data_reshape)
    if prediction == 1:
        return "Diabetes Confirmed"
    else:
        return "No Diabetes"
    
def main():
    #Give title to page
    st.title("Diabetes Prediction")
    
    #Getting the input values
    Pregnancies = st.text_input("No. of Pregnancies")
    Glucose= st.text_input("Glucose Level")
    BloodPressure = st.text_input("BP Level")
    SkinThickness= st.text_input("SkinThickness")
    Insulin= st.text_input("Insulin")
    BMI= st.text_input("BMI")
    DiabetesPedigreeFunction =  st.text_input("Diabetes Pedigree Function")
    Age = st.text_input("Age")

    diagnosis = ''

    if st.button("Test"):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,
                                         Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)


if __name__ == '__main__':
    main()
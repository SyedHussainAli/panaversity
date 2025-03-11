import streamlit as st
import pandas as pd

st.title('BMI Calculator')

height = st.slider('Enter your height in cm:', 100, 250, 150)
weight = st.slider('Enter your weight in kg:', 30, 200, 70)

bmivalue = weight / ((height/100) ** 2)

st.write(f'Your BMI is: {bmivalue:.2f} ')

st.write('## BMI Categories: ##')
st.write('- Underweight = <18.5')
st.write('- Normal weight = 18.5 – 24.9')
st.write('- Overweight = 25 – 29.9')
st.write('- Obesity = BMI of 30 or greater')
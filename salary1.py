import pandas as pd
import numpy as np
import joblib
import streamlit as st


st.set_page_config(page_title="My Program", page_icon="🚀", layout="centered")


menu = st.sidebar.radio("📌 Navigation", ["Home", "About", "Contact"])

model = joblib.load("salary_prediction.joblib")
st.title("SALARY PREDICTOR 💸")

if menu == "Home":
    exp = st.number_input("Enter Experience in years :",min_value=0)
    
    btn = st.button("CLICK HERE")
    if btn:
        m = model.coef_[0]
        b = model.intercept_
        y = m * exp + b

        st.success(f"Your Salary will be : {str(y)[:8]} Per Month")
        st.snow()

elif menu == "About":
    st.title("ℹ️ About")
    st.write("""
    The Salary Predictor is a Machine Learning web application built using Python, Streamlit, and Scikit-learn.
             It allows users to predict their monthly salary based on their years of experience.
             
                    Salary=(Coefficient×Experience)+Intercept
                            🚀 Made with ❤️ by Me
    """)

elif menu == "Contact":
    st.title("📧 Contact")
    st.write("For queries : Email : Shabeermadhlotia26@gmail.com")
    st.write("🅾  𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 : https://www.instagram.com/shabeer_26?igsh=MWpxYmdzZ3Nmd29jYQ%3D%3D&utm_source=qr")
    st.write("🅾  𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 : https://www.instagram.com/imnot__abhay?igsh=MTU0dGZydjJybGRhaw%3D%3D&utm_source=qr")
    
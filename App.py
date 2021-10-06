import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import pandas as pd
st.set_option('deprecation.showfileUploaderEncoding', False)

model = pickle.load(open('car_prediction.pkl', 'rb'))

def predict_price(Present_Price,Kms_Driven,Owner,Years_old,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual):
  input = np.array([[Present_Price,Kms_Driven,Owner,Years_old,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]]).astype(np.float64)
  prediction = model.predict(input)
  return float(prediction)

def main():
  st.title("CAR PRICE PREDICTIONS")
  html_temp ="""
  <div style="background-color:black; padding:10px">
  <h2 style="color:white;text-align:center;">CAR_PRICE_PREDICTIONS</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  Present_Price = st.text_input("Present Price")
  Kms_Driven = st.text_input("Kms Driven")
  Owner = st.text_input("Owner(0/1/3)")
  Years_old = st.text_input("Years old")
  Fuel_Type_Petrol = st.text_input("Fuel Type(Petrol/Diesel/CNG)")
  if Fuel_Type_Petrol=='Petrol':
    Fuel_Type_Petrol=0
    Fuel_Type_Diesel=1
  elif Fuel_Type_Petrol=='Diesel':
    Fuel_Type_Petrol=1
    Fuel_Type_Diesel=0
  else:
    Fuel_Type_Petrol=0
    Fuel_Type_Diesel=0
    
  Seller_Type_Individual = st.text_input("Seller Type(Dealer/Individual)")
  if Seller_Type_Individual=="Dealer":
    Seller_Type_Individual=0
  else:
    Seller_Type_Individual=1

  Transmission_Manual = st.text_input("Transmission(Manual/Automatic)")
  if Transmission_Manual=="Manual":
    Transmission_Manual=1
  else:
    Transmission_Manual=0

  
  
  
  if st.button("Predict"):
    output = predict_price(Present_Price,Kms_Driven,Owner,Years_old,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual)
    st.success(round(output))

  if st.button("About"):
    st.header("By Aman Jain")
    st.subheader("Summer Internship")
  
if __name__=='__main__':
  main()

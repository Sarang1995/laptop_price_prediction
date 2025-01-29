import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("model.joblib")

st.title('Laptop Price Prediction Project')
st.markdown('We used Regression model to predict a Laptop price')



data = pd.read_csv("X_train.csv")

company = st.selectbox('Pick your company', data["company"].unique().tolist())
typename = st.selectbox('Pick your type name', data["typename"].unique().tolist())
screenresolution = st.selectbox('Pick your screenresolution', data["screenresolution"].unique().tolist())
ram = st.selectbox('Pick your Ram', data["ram"].unique().tolist())
opsys = st.selectbox('Pick your Operating System', data["opsys"].unique().tolist())
ssd = st.selectbox('You want SSD in you laptop', data["ssd"].unique().tolist())
hdd = st.selectbox('You want HDD in you laptop', data["hdd"].unique().tolist())
ips = st.radio('You want IPS in your laptop', data["ips"].unique().tolist())
touchscreen = st.radio('You want Touchscreen laptop', data["touchscreen"].unique().tolist())
flash_storage = st.radio('You want flash_storage in you laptop', data["flash_storage"].unique().tolist())
gpu_brand = st.selectbox('Pick your GPU brand', data["gpu_brand"].unique().tolist())
cpu_brand = st.selectbox('Pick your CPU barnd', data["cpu_brand"].unique().tolist())


input_data = pd.DataFrame([[company,typename,screenresolution,ram,opsys,ips,
                          touchscreen,ssd,hdd,flash_storage,gpu_brand,cpu_brand]],
                          columns = ['company','typename','screenresolution','ram','opsys','ips',
                          'touchscreen','ssd','hdd','flash_storage','gpu_brand','cpu_brand'])

st.dataframe(input_data)

if st.button('Predict'):
    prediction = round(np.exp(model.predict(input_data)[0]),2)
    st.success(f"Predicted Laptop Price: ${prediction}")
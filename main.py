import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# model_path = "C:/Users/yogesh/Desktop/Flask/Laptop Price Prediction/final_model.joblib"
# Get the directory where the script is running
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Use a relative path
model_path = os.path.join(BASE_DIR, "final_model.joblib")

model = joblib.load(model_path)

st.title('Laptop Price Prediction Project')
st.markdown('We used Regression model to predict a Laptop price')

data = pd.read_csv("X_train.csv")
X_test = pd.read_csv('X_test.csv')
y_test = pd.read_csv("y_test.csv")

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
    prediction = round(model.predict(input_data)[0],2)
    st.success(f"Predicted Laptop Price INR: {prediction}")


tab1, tab2, tab3 = st.tabs(['R2_score', 'Mean Absolute Error', 'Mean Root Square Error'])

with tab1:
    st.header('R2_score')
    score = round((r2_score(y_test, model.predict(X_test)))*100, 2)
    st.success(f"r2_score: {score}%")

with tab2:
    st.header('Mean Absolute Error')
    mean_absolute_error_score = round(mean_absolute_error(y_test, model.predict(X_test)), 4)
    st.success(f"Mean Absolute Error: {mean_absolute_error_score}")

with tab3:
    st.header('Root Mean Squared Error')
    RMSE = round(np.sqrt(mean_squared_error(y_test, model.predict(X_test))), 4)
    st.success(f"Root Mean Squared Error: {RMSE}")
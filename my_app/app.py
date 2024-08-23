import streamlit as st
from controller.GetPrediction import GetPrediction
from controller.LoadModel import LoadModel

st.title("📱 Mobile Price Predictor")
st.write("Enter the characteristics of the mobile phone to predict its price.")

battery_power = st.slider("🔋 Battery Power (mAh)", 500, 2000, step=1)
px_height = st.slider("📏 Pixel Height", 0, 2000, step=1)
px_width = st.slider("📐 Pixel Width", 500, 2000, step=1)
ram = st.slider("💾 RAM (MB)", 256, 4000, step=1)

st.write(f"**Battery Power:** {battery_power} mAh")
st.write(f"**Pixel Height:** {px_height}")
st.write(f"**Pixel Width:** {px_width}")
st.write(f"**RAM:** {ram} MB")

import pickle
with open('model\mobile_price_prediction_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

list_of_features = [battery_power, px_height, px_width, ram]

if st.button("🔮 Predict Price"):
    prediction = GetPrediction(loaded_model, list_of_features)

    st.success(f"Price Category: {prediction}")
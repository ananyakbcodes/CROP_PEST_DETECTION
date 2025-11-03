import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model
import joblib

st.set_page_config(page_title="Crop Disease & Weather Risk Predictor", page_icon="🌿")

st.title("🌾 Crop Disease & Weather Risk Prediction System")

# Load models (from root folder — not inside /models)
cnn_model = load_model("cnn_model.h5")
weather_data = joblib.load("weather_model.pkl")
weather_model = weather_data["model"]

uploaded_img = st.file_uploader("📸 Upload a leaf image", type=["jpg", "jpeg", "png"])
temp = st.number_input("🌡 Temperature (°C)", min_value=0, max_value=50, value=30)
humidity = st.number_input("💧 Humidity (%)", min_value=0, max_value=100, value=65)
rainfall = st.number_input("🌧 Rainfall (mm)", min_value=0, max_value=50, value=10)

if st.button("Predict"):
    if uploaded_img is None:
        st.warning("Please upload an image first!")
    else:
        # Image preprocessing
        img = cv2.imdecode(np.frombuffer(uploaded_img.read(), np.uint8), 1)
        img = cv2.resize(img, (128, 128))
        img = img / 255.0
        img = np.expand_dims(img, axis=0)

        # Disease prediction
        pred = cnn_model.predict(img)
        disease_id = int(np.argmax(pred))
        confidence = round(100 * np.max(pred), 2)

        # Weather risk prediction
        weather_input = np.array([[temp, humidity, rainfall, 1000, 3]])
        risk_pred = weather_model.predict(weather_input)[0]

        st.subheader("🌿 Prediction Results")
        st.write(f"**Disease Class ID:** {disease_id} ({confidence}% confidence)")
        st.write(f"**Risk Level:** {'⚠️ High' if risk_pred == 1 else '✅ Low'}")

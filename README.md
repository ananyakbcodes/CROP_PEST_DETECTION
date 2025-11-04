

#  Crop Pest Detection

This project aims to **predict crop pest infestations** using a combination of **weather data** and **image-based deep learning analysis**.
It integrates a **CNN model** for pest image classification with a **weather-based Random Forest model** to assess outbreak risk, wrapped into an easy-to-use application interface.

---

## Project Overview

The **Crop Pest Detection System** helps farmers and researchers detect pest risks early using two complementary components:

1. **Weather-based Model** – Predicts the likelihood of pest outbreaks from live temperature, humidity, and precipitation data.
2. **CNN-based Model** – Classifies pests from crop leaf images using convolutional neural networks.
3. **Integrated Application** – Combines both models into a unified, interactive tool for real-time pest risk analysis.

---

## Team Contributions

### **Ananya – CNN Model Development**

* Designed and trained a **Convolutional Neural Network (CNN)** for pest image classification.
* Optimized model accuracy through hyperparameter tuning and dataset augmentation.
* Documented and saved the trained model in `cnn_model.ipynb`.

### **Cassiel – Weather Model Development**

* Developed a **Random Forest regression model** using real-time data from the **OpenWeatherMap API**.
* Preprocessed, cleaned, and structured weather data for training.
* Key files:

  * `3_train_weather_model.ipynb` – Weather data collection and model training
  * `models/weather_model.pkl` – Trained model file
  * `crop_pest_detection.tex` – LaTeX research report on model design and evaluation

### **Aaliyah – Model Integration**

* Integrated the CNN and weather models into a **unified prediction pipeline**.
* Ensured smooth communication between submodules and consistent data flow.
* Implemented the decision logic for generating combined pest risk scores.

### **Pranita – Image Preprocessing & Dashboard Interface**

* Handled **image preprocessing**, including resizing, normalization, and augmentation.
* Supported **front-end Streamlit development**, linking user uploads to model inference.
* Helped test and debug the dashboard for real-time predictions and usability.

---

##  System Architecture

The system follows a modular, four-layer pipeline ensuring scalability and real-time performance:

1. **Data Acquisition Layer**

   * Collects pest images and live weather data via OpenWeatherMap API.
   * Performs image preprocessing and data cleaning.

2. **Modeling Layer**

   * CNN for image-based pest classification.
   * Random Forest regression for weather-based outbreak prediction.

3. **Integration Layer**

   * Combines outputs from both models.
   * Applies logic to determine final pest risk assessment.

4. **Presentation Layer**

   * Built using **Streamlit** for visualization and interaction.
   * Allows image uploads, weather data display, and unified risk predictions.

---

##  Project Structure

```
.
├── models/
│   ├── cnn_model.h5
│   ├── weather_model.pkl
│
├── scripts/
│   ├── app.py
│   ├── integration.py
│
├── notebooks/
│   ├── cnn_model.ipynb
│   ├── 3_train_weather_model.ipynb
│
├── reports/
│   ├── crop_pest_detection.tex
│   ├── crop_pest_detection.pdf
│
├── README.md
└── requirements.txt
```

---

##  Setup Instructions

### **1️ Clone the Repository**

```bash
git clone https://github.com/yourusername/crop-pest-detection.git
cd crop-pest-detection
```

### **2️ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3️ Run the Application**

```bash
streamlit run scripts/app.py
```

### **4️ Upload and Predict**

* Upload an image of a pest-infected crop.
* The system will classify the pest type and generate a **weather-adjusted risk score**.

---

##  Results Summary

| Model                              | Dataset Size   | Accuracy / R² Score |
| ---------------------------------- | -------------- | ------------------- |
| CNN (Pest Classification)          | 3,200 images   | **91.7%**           |
| Random Forest (Weather Prediction) | 1,000+ samples | **88.4%**           |

---

##  Future Enhancements

* Integrate **IoT-based sensors** for automated data collection.
* Expand model training to include **multi-crop and region-specific pests**.
* Build a **mobile-optimized interface** for farmers.
* Add **Explainable AI (XAI)** support for interpretability.

---


---


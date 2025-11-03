## Crop Pest Detection – Weather Model Component

This part includes the weather-based model and related documentation used for the Crop Pest Detection project.

### Files Included
- `3_train_weather_model.ipynb` – Notebook that collects live weather data, trains a Random Forest model, and saves it for later use.  
- `models/weather_model.pkl` – Trained Random Forest model saved in serialized format.  
- `crop_pest_detection.tex` – Tex file of the lateX report describing the model and its role in the Crop Pest Detection system.
- `crop_pest_detection.pdf` – LaTeX report 

### Description
The notebook uses the OpenWeatherMap API to gather real-time weather data from multiple cities in India.  
A Random Forest classifier analyzes temperature, humidity, rainfall, and other factors to determine favorable crop conditions.  
The final trained model is stored as a `.pkl` file, and the accompanying LaTeX report explains the method and results.



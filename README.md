# Final Model Integration (My Contribution)

In this part of the project, I integrated the two trained models:
1. The **CNN model** that predicts the disease from the leaf image.
2. The **Weather model** that predicts the risk level based on temperature, humidity, and rainfall.

The goal of my work was to combine both models into one final working pipeline that takes user input and returns a clear output.

---

## What My Code Does
- Loads the saved `cnn_model.h5` and `weather_model.pkl`
- Preprocesses the input leaf image
- Runs disease prediction using the CNN
- Takes weather values from the user
- Predicts **Low / Medium / High** disease risk
- Prints both results together in a clean format

---

## Main File (My Work)

**`final_pipeline.ipynb`**  
This notebook:
- Performs the integration
- Defines the `predict_disease_and_risk()` function
- Produces the final combined output

---

## How to Use (For Testing)
1. Upload:
   - `cnn_model.h5`
   - `weather_model.pkl`
   - A leaf image
2. Run `final_pipeline.ipynb`
3. Call the function:

```python
predict_disease_and_risk("leaf.jpg", 30, 70, 10)

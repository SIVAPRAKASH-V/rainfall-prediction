# Rainfall Prediction App

## Overview
This is a Python-based GUI application designed to predict whether it will rain or not. The app uses the `tkinter` library for the user interface and integrates a pre-trained machine learning model to make predictions. The machine learning model is built using an ensemble-based stacking algorithm and leverages data from the Australian weather dataset.

## Features
- Simple and user-friendly GUI built with `tkinter`.
- Predicts rainfall using a pre-trained machine learning model stored as a `.pkl` file.
- Incorporates advanced ensemble-based stacking for improved accuracy.
- Preprocessing and feature selection steps were performed on the dataset to ensure optimal model performance.

## Dataset
The machine learning model was trained on the Australian weather dataset, which includes various meteorological features. Key steps in the dataset preparation include:
- **Data Preprocessing:** Handling missing values, encoding categorical features, and normalizing numerical data.
- **Feature Selection:** Identifying and selecting the most relevant features for prediction.
- for detailed process add comments.

## Machine Learning Model
- **Algorithm:** Ensemble-based stacking.
- **Purpose:** Combines multiple base models to improve prediction performance.
- **Format:** Saved as a `.pkl` file for easy integration with the app.

## Prerequisites
Before running the app, ensure you have the following installed:
- Python 3.x
- Required Python libraries:
  - `tkinter`
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `joblib`

Install dependencies using:
```bash
pip install pandas numpy scikit-learn
```

## How to Run the App
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/rainfall-prediction-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd rainfall-prediction-app
   ```
3. Ensure the pre-trained model file (`model.pkl`) is present in the project directory. Extract it from zip file.
4. Run the Python script to launch the app:
   ```bash
   python app.py
   ```
5. Input the required meteorological features into the GUI and click the "Predict" button to see the prediction result.


## License
Give credits to author in all places 
## Acknowledgments
- Australian weather dataset: Source of data for training the model.
- Python and its libraries for providing the tools to build this application.
---
<p>For detailed instructions and troubleshooting, please comment or contact the author.</p>
<p>Give Credits to the author</p>
<p>If you like this project give stars.</p>

### Thank you

# **Author**: _Sivaprakash V_

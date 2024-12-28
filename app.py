import tkinter as tk 
from PIL import Image, ImageTk 
from tkinter import messagebox 
import numpy as np 
from sklearn.ensemble import RandomForestClassifier 
import joblib 
model = joblib.load(".\rain_pred.pkl")   
def predict_result(params): 
    params_array = np.array(params).reshape(1, -1) 
    prediction = model.predict(params_array) 
    return prediction[0] 
def on_predict(): 
    sunshine = float(sunshine_entry.get()) 
    cloud9am = float(cloud9am_entry.get()) 
    cloud3pm = float(cloud3pm_entry.get()) 
    humidity3pm = float(humidity3pm_entry.get()) 
    pressure9am = float(pressure9am_entry.get()) 
    print(f"Sunshine: {sunshine}") 
    print(f"Cloud9am: {cloud9am}") 
    print(f"Cloud3pm: {cloud3pm}") 
    print(f"Humidity3pm: {humidity3pm}") 
    print(f"Pressure9am: {pressure9am}") 
    # Predict the result 
    result = predict_result([sunshine, cloud9am, cloud3pm, humidity3pm, pressure9am]) 
    # Map the prediction result to the respective image 
    if result == 1: 
        image_path = ".\rain.png" 
    else: 
        image_path = ".\no.png" 
    image_window = tk.Toplevel() 
    image_window.title("Image Viewer") 
    image = Image.open(image_path) 
    image = image.resize((500, 500)) 
    photo = ImageTk.PhotoImage(image) 
    # Display the image 
    image_label = tk.Label(image_window, image=photo) 
    image_label.image = photo 
    image_label.pack() 
# Create the main application window 
root = tk.Tk() 
root.title("Rain Predictor") 
# Create a frame to center the input fields and button 
frame = tk.Frame(root) 
frame.pack(expand=True) 
label_font = ("Times New Roman", 14)  # Adjust the font size as needed 
entry_width = 20  # Adjust the width as needed 
sunshine_label = tk.Label(frame, text="Sunshine:", font=label_font) 
sunshine_label.grid(row=0, column=0, padx=5, pady=5, sticky="e") 
sunshine_entry = tk.Entry(frame, width=entry_width) 
sunshine_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w") 
cloud9am_label = tk.Label(frame, text="Cloud9am:", font=label_font) 
cloud9am_label.grid(row=1, column=0, padx=5, pady=5, sticky="e") 
cloud9am_entry = tk.Entry(frame, width=entry_width) 
cloud9am_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w") 
cloud3pm_label = tk.Label(frame, text="Cloud3pm:", font=label_font) 
cloud3pm_label.grid(row=2, column=0, padx=5, pady=5, sticky="e") 
cloud3pm_entry = tk.Entry(frame, width=entry_width) 
cloud3pm_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w") 
humidity3pm_label = tk.Label(frame, text="Humidity3pm:", font=label_font) 
humidity3pm_label.grid(row=3, column=0, padx=5, pady=5, sticky="e") 
humidity3pm_entry = tk.Entry(frame, width=entry_width) 
humidity3pm_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w") 
pressure9am_label = tk.Label(frame, text="Pressure9am:", font=label_font) 
pressure9am_label.grid(row=4, column=0, padx=5, pady=5, sticky="e") 
pressure9am_entry = tk.Entry(frame, width=entry_width) 
pressure9am_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w") 
# Create a button to predict 
predict_button = tk.Button(frame, text="Predict", command=on_predict) 
predict_button.grid(row=5, columnspan=2, pady=10) 
# Start the application 
root.mainloop() 
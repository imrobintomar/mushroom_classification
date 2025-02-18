import joblib
import numpy as np
import pandas as pd
from utils.constants import MODEL
from src.inputs.input_handler import get_user_input
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Load the model
model = joblib.load(MODEL)

# Define the feature names
feature_names = [
    "cap-diameter",
    "cap-shape",
    "gill-attachment",
    "gill-color",
    "stem-height",
    "stem-width",
    "stem-color",
    "season",
]

# Define the class mapping
class_mapping = {0: "Edible", 1: "Poisonous"}

while True:
    # Get user input
    user_input = get_user_input()

    if user_input is None:
        break

    # Convert input to DataFrame with feature names
    features = pd.DataFrame([user_input], columns=feature_names)

    # Make prediction
    prediction = model.predict(features)

    # Map the predicted class to a human-readable label
    predicted_class = class_mapping[prediction[0]]

    # Display the prediction result with color
    if prediction[0] == 1:
        print(f"{Fore.RED}[+] Predicted class: {predicted_class}{Style.RESET_ALL}\n")
    else:
        print(f"{Fore.GREEN}[+] Predicted class: {predicted_class}{Style.RESET_ALL}\n")

import pandas as pd
import joblib

loaded_rf_model = joblib.load('rf_model.joblib')

print("\n========================================")
print(" 🚴 QUICK BIKE DEMAND PREDICTOR 🚴 ")
print("========================================")

# 1. Ask 3 quick, intuitive questions
print("\n[1] Spring  [2] Summer  [3] Fall  [4] Winter")
season = float(input("Select the Season (1-4): "))

print("\n[1] Clear  [2] Cloudy/Mist  [3] Rain/Snow")
weather = float(input("Select the Weather (1-3): "))

print("\n[1] Cold  [2] Mild  [3] Hot")
temp_choice = input("Select the Temperature (1-3): ")

# 2. Translate human input to model numbers
temp_map = {'1': 0.2, '2': 0.5, '3': 0.8}
temp_val = temp_map.get(temp_choice, 0.5) # Defaults to mild if they type something wrong

# 3. Auto-fill the boring data in the background (Year 2, June, Wednesday, Working Day, Avg Humidity)
input_data = pd.DataFrame({
    'season': [season], 'yr': [1], 'mnth': [6], 'holiday': [0], 
    'weekday': [3], 'workingday': [1], 'weathersit': [weather], 
    'temp': [temp_val], 'atemp': [temp_val + 0.05], 'hum': [0.6], 'windspeed': [0.2]
})

# 4. Predict
prediction = loaded_rf_model.predict(input_data)

print("\n========================================")
print(f" ✅ PREDICTED RENTALS: {int(prediction[0])} bikes")
print("========================================\n")
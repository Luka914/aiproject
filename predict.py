import pandas as pd
import joblib

# Load the trained Random Forest model from the joblib file (meaning you don't have to retrain it every time)
loaded_rf_model = joblib.load('rf_model.joblib')

def predict_demand(model, temp, humidity, windspeed, weather_situation):
    """Predicts bike demand based on user input parameters."""
    
    input_data = pd.DataFrame({
        'season': [3], 'yr': [1], 'mnth': [8], 'holiday': [0], 
        'weekday': [3], 'workingday': [1], 'weathersit': [weather_situation], 
        'temp': [temp], 'atemp': [temp + 0.05], 'hum': [humidity], 'windspeed': [windspeed]
    })
    
    prediction = model.predict(input_data)
    
    # Optional: Print it to the screen so you can read it
    print(f"Predicted Bike Rentals: {int(prediction[0])}")
    
    # CRITICAL: Return the raw number back to the system
    return int(prediction[0])

#Testing the function with a sample input
final_prediction = predict_demand(loaded_rf_model, temp=0.7, humidity=0.6, windspeed=0.2, weather_situation=1)

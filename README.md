# Bike Rental Demand Prediction

There are a lot of variables affecting the demand for bicycle rentals, including but not limited to time of the day, weather, and day of the week. The ability to foresee the fluctuations in demand would help bicycle sharing companies to be ready for busy periods.

## Project Demo

<img width="541" height="430" alt="Animation" src="https://github.com/user-attachments/assets/ece72eeb-1573-4ee2-816e-ea860dd9bc5b" />


This research project will focus on training a machine learning model based on the past bicycle rental information provided for the city of Washington, D.C.

Specifically, I will analyze the data and train a model based on Python. It will also include the comparison between predictions made by the model and the reality.


## Installation

Clone the repository:

    git clone [YOUR_GITHUB_REPOSITORY_URL](https://github.com/Luka914/aiproject.git)

Enter the project directory:

    cd aiproject

Install dependencies:

    pip install -r requirements.txt

Train the model (you must do this first to generate the saved model file):

    python train.py

Run the predictor:

    python predict_updated.py



## 📊 Model Performance
I tested two models to see which was more accurate using Root Mean Squared Error (RMSE):

Linear Regression: Built first to get a baseline score.

Random Forest Regressor: Handled the non-linear weather patterns much better and dropped the RMSE, so this is the active model used in predict.py.


## Dataset and Credit

This project uses the [Bike Sharing Dataset](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset) from the UCI Machine Learning Repository.

Citation:

Fanaee-T, H. (2013). *Bike Sharing* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894

The dataset is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).

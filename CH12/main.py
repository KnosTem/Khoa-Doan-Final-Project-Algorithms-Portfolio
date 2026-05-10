import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def load_bakery_data():
    """
    Load the bakery data with weather, weekend/holiday, game status, and loaves sold.
    Returns a pandas DataFrame with the bakery data.
    """
    # Create the bakery dataset with hardcoded values
    data = {
        'weather': [3, 5, 2, 4, 1, 5, 3, 4, 2, 5, 1, 3, 4, 2, 5, 3, 4, 1, 2, 4],
        'weekend_holiday': [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
        'game_on': [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
        'loaves': [42, 95, 30, 72, 38, 55, 78, 50, 58, 85, 22, 52, 88, 44, 70, 65, 62, 48, 70, 75]
    }
    return pd.DataFrame(data)

def prepare_features_and_target(df):
    """
    Separate the features (weather, weekend_holiday, game_on) from the target (loaves).
    Returns X (features) and y (target) as numpy arrays.
    """
    # TODO: Extract the feature columns (weather, weekend_holiday, game_on) into X
    # Hint: Use df[['column1', 'column2', 'column3']].values to get numpy array
    X = df[['weather', 'weekend_holiday', 'game_on']].values
    
    # TODO: Extract the target column (loaves) into y
    # Hint: Use df['column_name'].values to get numpy array
    y = df['loaves'].values
    
    return X, y

def train_knn_model(X, y, k=4):
    """
    Train a KNN regression model with k neighbors.
    Returns the trained model.
    """
    # TODO: Create a KNeighborsRegressor with n_neighbors=k
    # Hint: Use KNeighborsRegressor(n_neighbors=k)
    model = KNeighborsRegressor(n_neighbors=k)
    
    # TODO: Fit the model using X and y
    # Hint: Use model.fit(X, y)
    model.fit(X, y)
    
    return model

def predict_loaves_for_today(model, weather, weekend_holiday, game_on):
    """
    Predict how many loaves to bake for today given the conditions.
    Returns the predicted number of loaves.
    """
    # TODO: Create a feature array for today's conditions
    # Hint: Use np.array([[weather, weekend_holiday, game_on]])
    today_features = np.array([[weather, weekend_holiday, game_on]])
    
    # TODO: Use the model to predict loaves for today
    # Hint: Use model.predict(today_features) and get the first element
    prediction = model.predict(today_features)[0]
    
    return prediction

def main():
    """
    Main function to demonstrate KNN regression for bakery loaf prediction.
    Today's conditions: weekend day with good weather (weather=4, weekend_holiday=1, game_on=0)
    """
    # Load the bakery data
    df = load_bakery_data()
    print("Bakery Data:")
    print(df)
    print()
    
    # Prepare features and target
    X, y = prepare_features_and_target(df)
    print("Features shape:", X.shape if X is not None else "Not implemented")
    print("Target shape:", y.shape if y is not None else "Not implemented")
    print()
    
    # Train KNN model with k=4
    model = train_knn_model(X, y, k=4)
    print("KNN model trained with k=4")
    print()
    
    # Today's conditions: weekend day with good weather
    today_weather = 4  # Good weather (scale 1-5)
    today_weekend_holiday = 1  # It's a weekend
    today_game_on = 0  # No game today
    
    print(f"Today's conditions: Weather={today_weather}, Weekend/Holiday={today_weekend_holiday}, Game={today_game_on}")
    
    # Predict loaves for today
    predicted_loaves = predict_loaves_for_today(model, today_weather, today_weekend_holiday, today_game_on)
    print(f"Predicted loaves to bake: {predicted_loaves if predicted_loaves is not None else 'Not implemented'}")
    
    # Create a simple visualization of the data
    plt.figure(figsize=(10, 6))
    plt.scatter(df['weather'], df['loaves'], alpha=0.7, label='Historical Data')
    plt.xlabel('Weather (1-5 scale)')
    plt.ylabel('Loaves Sold')
    plt.title('Bakery Sales vs Weather')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.close()
    
if __name__ == "__main__":
    main()

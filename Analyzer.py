import requests
import json
from collections import Counter

starting = ""
destination = ""

import pandas as pd
import joblib
from sklearn.preprocessing import OneHotEncoder, StandardScaler
rf_model_path = os.path.join("model", "random_forest_model.pkl")
rf_model_loaded = joblib.load(rf_model_path)
ohe_path = os.path.join("model", "one_hot_encoder.pkl")
ohe_loaded = joblib.load(ohe_path)

def predict_speed(data):
    
    categorical_features = ['Service Provider', 'Technology', 'Test_type', 'LSA']

    encoded_new_data = ohe_loaded.transform(data[categorical_features])
    X_new = pd.DataFrame(encoded_new_data, columns=ohe_loaded.get_feature_names_out())

    predicted_speed = rf_model_loaded.predict(X_new)
    print("Predicted Data Speed (Mbps):", predicted_speed)

    return predicted_speed[0]



def analyze_payments(start_location, end_location):
    # Call the API to get nearby restaurants
    url = "https://tempapi-a7a9f8f8dpbaf5gv.centralindia-01.azurewebsites.net/nearby-restaurants"
    params = {
        "start_location": start_location,
        "end_location": end_location,
        "num_restaurants": 15
    }

    #GooglePlaceAPI.generate_nearby_restaurants(15,start_location,end_location)

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        nearby_restaurants = response.json()
        payment_counter = Counter()

        for restaurant in nearby_restaurants:
            if restaurant.get('paymentOptions'):
                for option in restaurant['paymentOptions']:
                    if option:
                        payment_counter[option] += 1

        total_digital = payment_counter.get('Digital-Payment', 0)
        total_cash = payment_counter.get('Cash', 0)


        if total_digital > total_cash:
            recommendation = "Digital Payments"
        elif total_cash > total_digital:
            recommendation = "Cash"
        else:
            recommendation = "Both"

        return recommendation
    else:
        return f"Failed to retrieve data: {response.status_code}"


# Example usage

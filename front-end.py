import streamlit as st
import requests


# streamlit run app.py

st.title("Spend Sense")

start_location = st.text_input("Enter Start Location")
end_location = st.text_input("Enter End Location")

network_provider = st.selectbox(
    "Select Network Service Provider",
    ["AIRTEL", "JIO", "VI", "BSNL"]
)

if network_provider=="VI":
    network_provider = "VODAFONE"

# Function to make an API call
import random
if st.button("Submit"):
    if start_location and end_location:
        url = "http://127.0.0.1:8002/predict"
        params = {
                "service_provider": network_provider,
                "network_type": "4G",
                "start_loc": "Delhi",
                "end_loc": "Andhra Pradesh"
                }
        prev_params = params

        respons = requests.post(url,json=params)
        # result = call_api(start_location, end_location, network_provider)
        # responses = [
        #     "Use Cash!",
        #     "Can rely on Digital Payments!",
        #     "Digital payments are widely accepted, but due to poor network signals of your carrier, use cash.",
        #     "Digital payments should be fine, but keep some cash handy just in case."
        # ]
        # response = random.choice(responses)

        if respons.status_code==200:
            temp_json = respons.json()
            final_suggestion = temp_json.get("response")
        else:
            final_suggestion = "Bad Request, check server is offline!"
        st.write("Suggestion:", final_suggestion)
    else:
        st.error("Please enter both Start and End valid locations.")

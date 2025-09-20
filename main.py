"""
Rain Alert SMS Notifier
-----------------------
This script checks the weather forecast using the OpenWeather API.
If rain is predicted in the next few hours, it sends an SMS reminder
via Twilio to carry an umbrella.
"""

import os
import requests
from twilio.rest import Client

# ------------------- Configuration -------------------
# Load sensitive keys from environment variables
ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN  = os.environ.get("TWILIO_AUTH_TOKEN")
API_KEY     = os.environ.get("OWM_API_KEY")

# OpenWeather endpoint
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

# Location (example: Singapore)
MY_LAT  = 1.352083
MY_LONG = 103.819839

# ------------------- Weather Check -------------------
params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4,  # check the next 4 forecast entries (~12 hours)
}

response = requests.get(OWM_ENDPOINT, params=params)
response.raise_for_status()
weather_data = response.json()

will_rain = any(
    int(hour["weather"][0]["id"]) < 700
    for hour in weather_data["list"]
)

# ------------------- SMS Notification -------------------
if will_rain:
    print("Rain expected. Sending SMS reminder...")
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="☔ Rain is expected today. Don’t forget your umbrella!",
        from_="+1XXXXXXXXXX",  # Replace with your Twilio number
        to="+XXXXXXXXXX"       # Replace with your verified number
    )
    print(f"Message sent: {message.sid}")
else:
    print("No rain expected. No SMS sent.")

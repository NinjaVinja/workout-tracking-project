from dotenv import load_dotenv
import os
load_dotenv()
import requests
from datetime import datetime

# loading all my keys from .env file
APP_ID = os.getenv("APP_ID")
NUTRITION_API_KEY = os.getenv("NUTRITION_API_KEY")
GOOGLE_SHEET_API_KEY = os.getenv("GOOGLE_SHEET_API_KEY")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")

# api endpoints
base_url = "https://app.100daysofpython.dev"
nutrition_and_exercise_endpoint = f"{base_url}/v1/nutrition/natural/exercise"
nutrition_and_exercise_healthz_endpoint = f"{base_url}/healthz"
google_sheet_endpoint = f"https://api.sheety.co/{GOOGLE_SHEET_API_KEY}/myWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": NUTRITION_API_KEY,
}

# ask user what exercise they did
exercise_params = {
    "query": input("Tell me which exercise you did: "),
    "weight_kg": 62,
    "height_cm": 180.34,
    "age": 22,
    "gender": "male",
}

# get calories burned from nutrition api
response = requests.post(nutrition_and_exercise_endpoint, headers=headers, json=exercise_params)
result = response.json()
print(result["exercises"][0])

# just checking if the api is up
status = requests.get(nutrition_and_exercise_healthz_endpoint)
print(status.json())

# get current data from the sheet
sheet_response = requests.get(url=google_sheet_endpoint, auth=(SHEETY_USERNAME, SHEETY_PASSWORD))
print(sheet_response.json())

today = datetime.today()

# preparing data to add in sheet
workouts = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "duration": result["exercises"][0]["duration_min"],
        "exercise": result["exercises"][0]["name"],
        "calories": result["exercises"][0]["nf_calories"],
    }
}

# adding the workout to google sheet
posting_data_on_sheet = requests.post(google_sheet_endpoint, json=workouts, auth=(SHEETY_USERNAME, SHEETY_PASSWORD))
print(posting_data_on_sheet.text)

# 🏋️ Workout Tracking Project

A simple Python app that logs your workouts automatically. Just tell it what exercise you did, and it calculates the calories burned and saves everything straight to your Google Sheet.

## How it works

1. You describe your exercise in plain English (e.g. *"ran 5 miles"* or *"swam for 1 hour"*)
2. The app sends this to the Nutrition & Exercise API, which calculates duration and calories burned
3. The workout details (date, time, duration, exercise, calories) get added as a new row in your Google Sheet using Sheety

## Tech Stack

- Python
- [Nutrition & Exercise API](https://app.100daysofpython.dev) — for calorie calculations from natural language
- [Sheety](https://sheety.co) — turns a Google Sheet into a usable API
- `python-dotenv` — for keeping API keys safe

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/NinjaVinja/workout-tracking-project.git
cd workout-tracking-project
```

### 2. Install dependencies

```bash
pip install requests python-dotenv
```

### 3. Create a `.env` file

In the project root, create a file named `.env` and add your own credentials:

```
APP_ID=your_app_id
NUTRITION_API_KEY=your_nutrition_api_key
GOOGLE_SHEET_API_KEY=your_sheety_project_key
SHEETY_USERNAME=your_sheety_username
SHEETY_PASSWORD=your_sheety_password
```

> ⚠️ Never commit your `.env` file. It's already listed in `.gitignore`.

### 4. Set up your Google Sheet

Your sheet should have these columns (in any order):

| Date | Time | Exercise | Duration | Calories |
|------|------|----------|----------|----------|

Connect it to Sheety and enable **Basic Authentication** on the endpoint so no one else can read/write your data.

### 5. Run the app

```bash
python main.py
```

You'll be asked to describe your exercise, and the workout will be logged in your sheet automatically.

## Example

```
Tell me which exercise you did: ran 5 miles
```

This calculates the calories burned and adds a new row to your Google Sheet with today's date, time, exercise name, duration, and calories.

## Notes

- Personal stats (weight, height, age, gender) are currently hardcoded in `main.py` — update them to match your own details for more accurate calorie estimates.
- Make sure `.env`, `.venv`, and `.idea` are all excluded from version control (already handled in `.gitignore`).

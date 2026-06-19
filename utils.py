import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

def calculate_bmi(weight,height):

    h=height/100

    bmi=weight/(h*h)

    return round(bmi,2)


def meal_plan(profile):

    prompt=f"""
    Create a personalized 7-day healthy meal plan.

    Age: {profile['age']}
    Weight: {profile['weight']}
    Height: {profile['height']}
    Goal: {profile['goal']}
    Allergy: {profile['allergy']}
    Fitness Level: {profile['fitness']}

    Include:
    Breakfast
    Lunch
    Dinner
    Calories
    Protein
    """

    response=model.generate_content(
        prompt
    )

    return response.text


def nutrition_chat(question):

    prompt=f"""
    You are a professional nutritionist.

    Answer:
    {question}
    """

    response=model.generate_content(
        prompt
    )

    return response.text


def analyze_food(image):

    prompt="""
    Analyze the food image.

    Tell:
    Food Name
    Estimated Calories
    Protein
    Fat
    Carbohydrate
    Health Advice
    """

    response=model.generate_content(
        [prompt,image]
    )

    return response.text
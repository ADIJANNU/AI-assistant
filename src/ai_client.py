import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_ai_response(message):
  for attempt in range(3):
    try:
      response = client.models.generate_content(
        model= "gemini-flash-latest",
        contents=message
      )
      return response.text
    except Exception as e:
      print(f"Attempt {attempt + 1} failed as {e}")
      time.sleep(10)
  return "Sorry, I couldn't get a response right now."

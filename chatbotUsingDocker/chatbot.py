import google.generativeai as genai
import os

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro")

def chat_with_gemini(user_input):
    response = model.generate_content(user_input)
    return response.text if response else "I'm sorry, I couldn't generate a response."

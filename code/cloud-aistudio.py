import google.generativeai as genai

YOUR_API_KEY = ""
genai.configure(api_key=YOUR_API_KEY)

try:
    model = genai.GenerativeModel('models/gemma-3-12b-it') 
    prompt = "Write a short poem about a dog."
    response = model.generate_content(prompt)
    print("\nResponse from models/gemma-3-12b-it:")
    print(response.text)
except Exception as e:
    print(f"Error {e}")
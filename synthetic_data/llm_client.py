import google.generativeai as genai
import os

class GeminiClient:
    def __init__(self, api_key=None, model_name="gemini-pro"):
        self.api_key = api_key or os.environ.get("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("Google API key not found. Set the GOOGLE_API_KEY environment variable.")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate_data(self, prompt):
        """Generates synthetic data using the Gemini model."""
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error generating data with Gemini: {e}")
            return None
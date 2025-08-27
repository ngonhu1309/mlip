from google import genai
from PIL import Image
import io
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

gemini_client = genai.Client(api_key=gemini_api_key)

def get_llm_response(image_data: bytes) -> str:
    image = Image.open(io.BytesIO(image_data))
    # implement the call to the Gemini API here
    # docs: https://ai.google.dev/gemini-api/docs/text-generation
    response = gemini_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=['Could you analyze this image in detail?', image]
    )
    return response.text
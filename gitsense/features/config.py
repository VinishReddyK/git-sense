import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    @staticmethod
    def get_api_keys():
        return {
            "gemini": os.getenv("GOOGLE_API_KEY")
        }
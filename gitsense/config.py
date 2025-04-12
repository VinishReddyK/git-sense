import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    @staticmethod
    def get_api_keys():
        # Load API keys from environment variables
        openai_key = os.getenv("OPENAI_API_KEY")
        google_key = os.getenv("GOOGLE_API_KEY")
        model_choice = os.getenv("LLM_MODEL", "openai").lower()
        
        if model_choice not in ["openai", "gemini"]:
            print(f"Warning: Unknown LLM_MODEL '{model_choice}'. Defaulting to openai.")
            model_choice = "openai"
            
        return {
            "openai": openai_key,
            "gemini": google_key,
            "model": model_choice
        }
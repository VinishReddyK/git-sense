import google.generativeai as genai
from .config import Config

class LLMProvider:
    def __init__(self):
        self.config = Config.get_api_keys()
        self._setup()
    
    def _setup(self):
        if not self.config.get("gemini"):
            raise ValueError("Google API key not configured in environment variables")
        genai.configure(api_key=self.config["gemini"])

    def ask(self, prompt, system_prompt=None):
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        full_prompt = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt
        
        response = model.generate_content(full_prompt)
        return response.text.strip()
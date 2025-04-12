import openai
import google.generativeai as genai
from .config import Config

class LLMProvider:
    def __init__(self, model=None):
        self.config = Config.get_api_keys()
        self.model = model or self.config["model"]
        self._setup()
    
    def _setup(self):
        if self.model == "openai":
            openai.api_key = self.config["openai"]
        elif self.model == "gemini":
            genai.configure(api_key=self.config["gemini"])

    def ask(self, prompt, system_prompt=None):
        if self.model == "openai":
            return self._ask_openai(prompt, system_prompt)
        else:
            return self._ask_gemini(prompt, system_prompt)

    def _ask_openai(self, prompt, system_prompt):
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            max_tokens=100,
            temperature=0.3
        )
        return response["choices"][0]["message"]["content"].strip()

    def _ask_gemini(self, prompt, system_prompt):
        model = genai.GenerativeModel('gemini-1.5-flash')
        full_prompt = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt
        response = model.generate_content(full_prompt)
        return response.text.strip()
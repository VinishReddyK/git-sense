import openai
import google.generativeai as genai
from .config import Config

class CommitMessageGenerator:
    def __init__(self):
        self.config = Config.get_api_keys()
        self._configure_apis()

    def _configure_apis(self):
        # Configure API clients based on selected model
        if self.config["model"] == "openai":
            openai.api_key = self.config["openai"]
        elif self.config["model"] == "gemini":
            genai.configure(api_key=self.config["gemini"])

    def generate(self, diff):
        # Generate commit message from diff
        prompt = self._build_prompt(diff)
        
        if self.config["model"] == "openai":
            return self._call_openai(prompt)
        else:
            return self._call_gemini(prompt)

    def _build_prompt(self, diff):
        return (
            "You are a helpful assistant that writes concise git commit messages.\n"
            "Write a short commit message summarizing the following diff:\n\n"
            "I want it to be clear and informative, but not too verbose. less than 10 words if possible.\n\n"
            "Here is the diff:\n\n"
            f"{diff}\n\nCommit message:"
        )

    def _call_openai(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50,
            temperature=0.3
        )
        return response["choices"][0]["message"]["content"].strip()

    def _call_gemini(self, prompt):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text.strip()
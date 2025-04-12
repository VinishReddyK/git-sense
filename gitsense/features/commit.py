# gitsense/commit.py
from .llm_provider import LLMProvider

class CommitMessageGenerator:
    def __init__(self):
        self.llm = LLMProvider()
    
    def generate(self, diff):
        system_msg = "You write great git commit messages. Keep them short (under 10 words if possible)."
        prompt = f"Write a commit message for these changes:\n\n{diff}\n\nMessage:"
        return self.llm.ask(prompt, system_msg)
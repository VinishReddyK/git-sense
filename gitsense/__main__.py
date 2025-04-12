#!/usr/bin/env python3

import subprocess
import openai
import sys
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Configure API keys, prioritizing environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")

# Default to OpenAI
model_choice = os.getenv("LLM_MODEL", "openai")

if model_choice == "openai" and not openai_api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    sys.exit(1)
elif model_choice == "gemini" and not google_api_key:
    print("Error: GOOGLE_API_KEY environment variable not set.")
    sys.exit(1)
elif model_choice not in ["openai", "gemini"]:
    print(f"Warning: Unknown LLM_MODEL '{model_choice}'. Defaulting to openai.")
    model_choice = "openai"

def get_git_diff():
    result = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True)
    return result.stdout

def generate_commit_message(diff, model=model_choice):
    prompt_base = (
        "You are a helpful assistant that writes concise git commit messages.\n"
        "Write a short commit message summarizing the following diff:\n\n"
        f"{diff}\n\nCommit message:"
    )

    if model == "openai":
        openai.api_key = openai_api_key
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt_base}],
            max_tokens=50,
            temperature=0.3
        )
        return response["choices"][0]["message"]["content"].strip()
    elif model == "gemini":
        genai.configure(api_key=google_api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt_base)
        return response.text.strip()
    else:
        raise ValueError(f"Unsupported model: {model}")

def stage_all_changes():
    subprocess.run(["git", "add", "."], check=True)

def commit_changes(message):
    subprocess.run(["git", "commit", "-m", message], check=True)

def main():
    if len(sys.argv) < 2 or sys.argv[1] != "commit":
        print("Usage: gitllm commit")
        print("Optional: Set LLM_MODEL environment variable to 'gemini' to use Gemini.")
        return

    stage_all_changes()
    diff = get_git_diff()
    if not diff:
        print("No changes staged for commit.")
        return

    commit_message = generate_commit_message(diff)
    print("\nSuggested commit message:")
    print(f"  {commit_message}")

    confirm = input("\nUse this message? (y/n): ").strip().lower()
    if confirm == 'y':
        commit_changes(commit_message)
        print("Changes committed.")
    else:
        print("Commit canceled.")
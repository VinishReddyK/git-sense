from .core.llm_provider import LLMProvider
from .core.git_utils import GitOperations
from .core.config import Config

class BranchNamer:
    def __init__(self):
        self.llm = LLMProvider()
        self.git = GitOperations()

    def generate_branch_name(self, diff):
        system_msg = """
        You generate short, descriptive Git branch names based on changes.
        Follow these rules:
        1. Use lowercase with hyphens (e.g., `fix/login-bug`).
        2. Prefix with:
           - `feat/` for new features,
           - `fix/` for bug fixes,
           - `refactor/` for code improvements.
        3. Keep it under 3-4 words.
        """
        prompt = f"Suggest a branch name for these changes:\n\n{diff}\n\nName:"
        return self.llm.ask(prompt, system_msg).strip()

    def create_branch(self, branch_name=None):
        diff = self.git.get_unstaged_diff()  # Get working directory changes
        
        if not diff:
            print("No changes detected. Using default branch name.")
            branch_name = "temp-branch"
        else:
            if not branch_name:
                branch_name = self.generate_branch_name(diff)
                print("Suggested branch name:")
                print(f"  {branch_name}")

                if Config.get_settings().ask_confirmation:
                    confirm = input("\nUse this name? (y/n): ").strip().lower()
                    if confirm != 'y':
                        print("Branch creation canceled.")
                        return 1

        self.git.create_new_branch(branch_name)
        print(f"Switched to branch: {branch_name}")
        return 0
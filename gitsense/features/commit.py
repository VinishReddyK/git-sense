from .core.llm_provider import LLMProvider
from .core.git_utils import GitOperations
from .core.config import Config
class CommitMessage:
    def __init__(self):
        self.llm = LLMProvider()
        self.git = GitOperations()

    def generate(self, diff):
        system_msg = "You write great git commit messages. Keep them short (under 10 words if possible)."
        prompt = f"Write a commit message for these changes:\n\n{diff}\n\nMessage:"
        return self.llm.ask(prompt, system_msg)
    
    def _commit(self):
        self.git.stage_all_changes()
        diff = self.git.get_staged_diff()
        
        if not diff:
            print("No changes staged for commit.")
            return 1

        commit_message = self.generate(diff)
        print("\nSuggested commit message:")
        print(f"  {commit_message}")

        if(Config.get_settings().ask_confirmation):
            confirm = input("\nUse this message? (y/n): ").strip().lower()
            if confirm == 'y':
                self.git.create_commit(commit_message)
                print("Changes committed.")
                return 0
            else:
                print("Commit canceled.")
                return 1
        else:
            print("No confirmation needed, proceeding with commit.")
            self.git.create_commit(commit_message)
            print("Changes committed.")
            return 0
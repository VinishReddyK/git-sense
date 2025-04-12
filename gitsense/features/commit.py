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
    
    def _commit(self, args=None):
        # Handle command line arguments
        custom_message = None
        stage_all = False
        
        if args:
            for arg in args:
                if arg.lower() == '-a':
                    stage_all = True
                elif not arg.startswith('-') and len(arg) > 0:
                    custom_message = arg
        
        # Stage changes
        if stage_all:
            self.git.stage_all_changes()
        
        # Get diff
        diff = self.git.get_staged_diff()
        
        if not diff:
            print("No changes staged for commit.")
            return 1

        # Use custom message if provided, otherwise generate one
        if custom_message:
            commit_message = custom_message
            print(f"Using provided commit message: {commit_message}")
        else:
            commit_message = self.generate(diff)
            print("Suggested commit message:")
            print(f"  {commit_message}")

        # Handle confirmation
        if Config.get_settings().ask_confirmation and not custom_message:
            confirm = input("\nUse this message? (y/n): ").strip().lower()
            if confirm != 'y':
                print("Commit canceled.")
                return 1

        # Create commit
        self.git.create_commit(commit_message)
        print("Changes committed.")
        return 0
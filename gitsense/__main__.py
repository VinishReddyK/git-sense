# gitsense/cli.py
import sys
from .features.git_utils import GitOperations
from .features.commit import CommitMessageGenerator

class CLI:
    def __init__(self):
        self.git = GitOperations()
        self.commit_gen = CommitMessageGenerator()

    def run(self, args):
        if len(args) < 2 or args[1] != "commit":
            self._show_usage()
            return 1

        return self._handle_commit()

    def _show_usage(self):
        print("Usage: gitsense commit")
        print("Optional: Set LLM_MODEL environment variable to 'gemini' to use Gemini.")
        return 1

    def _handle_commit(self):
        self.git.stage_all_changes()
        diff = self.git.get_staged_diff()
        
        if not diff:
            print("No changes staged for commit.")
            return 1

        commit_message = self.commit_gen.generate(diff)
        print("\nSuggested commit message:")
        print(f"  {commit_message}")

        confirm = input("\nUse this message? (y/n): ").strip().lower()
        if confirm == 'y':
            self.git.create_commit(commit_message)
            print("Changes committed.")
            return 0
        else:
            print("Commit canceled.")
            return 1

def main():
    cli = CLI()
    sys.exit(cli.run(sys.argv))
import subprocess

class GitOperations:
    @staticmethod
    def get_diff():
        # Get git all diff
        result = subprocess.run(["git", "diff", "HEAD"], 
                              capture_output=True, text=True)
        return result.stdout
    
    @staticmethod
    def get_staged_diff():
        # Get git diff of staged changes
        result = subprocess.run(["git", "diff", "--cached"], 
                              capture_output=True, text=True)
        return result.stdout
    
    @staticmethod
    def get_unstaged_diff():
        # Get diff of unstaged changes
        result = subprocess.run(
            ["git", "diff"],
            capture_output=True, text=True
        )
        return result.stdout

    @staticmethod
    def create_new_branch(branch_name):
        # Create and checkout a new branch
        subprocess.run(
            ["git", "checkout", "-b", branch_name],
            check=True
        )
    
    @staticmethod
    def stage_all_changes():
        # Stage all changes
        subprocess.run(["git", "add", "."], check=True)

    @staticmethod
    def create_commit(message):
        #Create a git commit with the given message
        subprocess.run(["git", "commit", "-m", message], check=True)
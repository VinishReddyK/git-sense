import sys
from .features.core.git_utils import GitOperations
from .features.commit import CommitMessage

class GitSense:
    def __init__(self):
        self.git = GitOperations()
        self.commit = CommitMessage()

    def run(self, args):
        if len(args) < 2:
            return self._show_usage()
        command = args[1]
        if command == "commit":
            return self.commit._commit()
        else:
            self._show_usage()
            return 1

    def _show_usage(self):
        print("Usage: gitsense commit")
        return 1

def main():
    gitsense = GitSense()
    sys.exit(gitsense.run(sys.argv))
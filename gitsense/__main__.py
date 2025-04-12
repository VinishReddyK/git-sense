import sys
from .features.core.git_utils import GitOperations
from .features.commit import CommitMessage

class CLI:
    def __init__(self):
        self.git = GitOperations()
        self.commit = CommitMessage()

    def run(self, args):
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
    cli = CLI()
    sys.exit(cli.run(sys.argv))
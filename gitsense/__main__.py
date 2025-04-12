import sys
from .features.core.git_utils import GitOperations
from .features.commit import CommitMessage
from .features.branch_namer import BranchNamer

class GitSense:
    def __init__(self):
        self.git = GitOperations()
        self.commit = CommitMessage()
        self.branch_namer = BranchNamer()

    def run(self, args):
        if len(args) < 2:
            return self._show_usage()

        command = args[1]
        handler = {
            'commit': self.commit._commit,
            'branch': self.branch_namer.create_branch,
            'help': self._show_help
        }.get(command, self._show_usage)

        return handler(args[2:])

    def _show_usage(self, _=None):
        print("Usage: gitsense <command> [options]")
        print("\nCommands:")
        print("  commit       Generate and commit changes based on staged changes")
        print("  branch       Generate a branch name based on all changes")
        print("  help         Show detailed help with options")
        return 1

    def _show_help(self, _=None):
        self._show_usage()
        print("\nOptions:")
        print("  commit:")
        print("    -a               Stage all changes before committing")
        print("    \"message\"      Use specified commit message instead of generating")
        print("\n  branch:")
        print("    \"name\"         Use specified branch name instead of generating")
        return 0

def main():
    gitsense = GitSense()
    sys.exit(gitsense.run(sys.argv))
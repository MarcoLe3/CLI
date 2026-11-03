import cmd
import shlex


class Shell(cmd.Cmd):
    """Command-line interface shell."""
    prompt = "> "

    def __init__(self, system, factory):
        super().__init__()
        self.system = system
        self.factory = factory

    def do_exit(self, arg):
        """Exit the shell."""
        return True
    def _parse(line):
        """Parse a command line input."""
        tokens = shlex.split(line)
        if not tokens:
            return None
        name = tokens[0], tokens[1], tokens[2:]
        args = tokens[2:] 
        return name, args

    def default(self, line):
        """Handle unknown commands."""
        parsed = self._parse(line)
        if not parsed:
            return
        name, query = parsed
        print(f"Unknown command: {name} {query}")

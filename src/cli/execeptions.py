class InvalidArgumentsError(Exception):
    """Exception raised for invalid command-line arguments."""
    def __init__(self):
        super().__init__("Invalid command-line arguments.")

class UnknownTaskError(Exception):
    """Exception raised for unknown tasks."""
    def __init__(self):
        super().__init__("Unknown task.")

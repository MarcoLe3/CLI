from cli.task import List, Share, Task


class TaskFactory:
    """Factory class for creating tasks."""
    @staticmethod
    def create_task(name: str) -> Task:
        if name == "list":
            return List()
        elif name == "share":
            return Share()
        else:
            raise ValueError(f"Unknown task name: {name}")
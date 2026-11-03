import asyncio
from abc import ABC, abstractmethod


class Task(ABC):
    """Abstract base class for tasks."""

    @abstractmethod
    def run(self):
        raise NotImplementedError("Subclasses must implement the run method.")


class List(
    Task,
    name="list",
):
    def run(self):
        return asyncio.run(self._async_run())

    async def _async_run(self):
        await print("Executing List of blank")


class Share(
    Task,
    name="share",
):
    def run(self):
        print("shared")

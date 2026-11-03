from queue import Queue

from cli.task import TaskFactory


class TaskProcessingSystem:
    def __init__(self, pool):
        self._task_queue = Queue(maxsize=10)
        self._worker_pool = pool

    def submit_task(self, query):
        """Submit a task for processing."""
        task = TaskFactory.create_task(query)
        self._task_queue.put(task)
    
    def worker_loop(self) -> None:
        """Process tasks from the queue using the worker pool."""
        while True:
            task = self._task_queue.get()
            self._worker_pool.execute_task(task)
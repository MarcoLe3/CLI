from queue import Queue
from threading import Thread


class WorkerPool:
    def __init__(self, pool_size: int):
        self._worker_pool = Queue(maxsize=pool_size)
        for _ in range(pool_size):
            self._worker_pool.put(Thread())

    def acquire(self) -> Thread:
        """Acquire a worker thread from the pool."""
        return self._worker_pool.get()

    def release(self, worker: Thread) -> None:
        """Release a worker thread back to the pool."""
        self._worker_pool.put(worker)

    def execute_task(self, task) -> None:
        """Execute a task using a worker thread from the pool."""
        try:
            worker = self.acquire()
            worker.start(target=task.run)
        finally:
            self.release(worker)

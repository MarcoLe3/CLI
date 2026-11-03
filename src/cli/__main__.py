import argparse

from cli.pool import WorkerPool
from cli.system import TaskProcessingSystem


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for the CLI."""
    parser = argparse.ArgumentParser(description="CLI")
    parser.add_argument("query", type=str, help="Task to execute")
    return parser


def main() -> None:
    args = build_parser().parse_args()

    task_system = TaskProcessingSystem(WorkerPool(pool_size=5))

    if task_system:
        task_system.submit_task(args.query)
        print(f"Task '{args.query}' submitted successfully.")
        task_system.worker_loop()

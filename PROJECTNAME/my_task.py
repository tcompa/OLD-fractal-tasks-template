"""
This is the Python module for my_task
"""

from pydantic.decorator import validate_arguments

@validate_arguments
def my_task(arg1: int) -> int:
    """
    This is the short description

    This is a long description. This is a long description. This is a long
    description. This is a long description. This is a long description.

    Args:
        arg1: description
    """
    return 1


if __name__ == "__main__":
    from fractal_tasks_core.tasks._utils import run_fractal_task

    run_fractal_task(task_function=my_task)

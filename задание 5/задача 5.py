import time
from typing import Callable, Any, Tuple
from pathlib import Path

def measure_execution_time(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Время выполнения {func.__name__}: "
              f"{execution_time:.6f} секунд")
        return result
    return wrapper


def read_numbers_from_file(file_path: Path) -> Tuple[int, int]:
    with open(file_path, "r") as file:
        numbers = file.read().strip().split()
        if len(numbers) < 2:
            raise ValueError("Файл должен содержать как минимум два числа")
        return int(numbers[0]), int(numbers[1])


def write_result_to_file(file_path: Path, result: int) -> None:
    with open(file_path, "w") as file:
        file.write(str(result))


@measure_execution_time
def calculate_sum(a: int, b: int) -> int:
    result = a + b
    print(f"Сумма чисел {a} и {b}: {result}")
    return result


@measure_execution_time
def process_file_calculation(input_path: Path, output_path: Path) -> None:
    a, b = read_numbers_from_file(input_path)
    result = calculate_sum(a, b)
    write_result_to_file(output_path, result)


if __name__ == "__main__":
    calculate_sum(10, 1)

    input_file = Path("input.txt")
    output_file = Path("output.txt")
    process_file_calculation(input_file, output_file)

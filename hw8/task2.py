TIME_DECIMALS = 8
PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
import time
from typing import Callable, Any


def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Декоратор для логирования времени выполнения функции.

    Args:
        func (Callable[..., Any]): Целевая функция, которую нужно обернуть.

    Returns:
        Callable[..., Any]: Обёрнутая функция (wrapper).
    """
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"{PERFORMANCE_LOG_PREFIX} функция '{func.__name__}' выполнена за {elapsed:.{TIME_DECIMALS}f} сек.")
        return result
    return wrapper

@performance_logger
def get_sorted_report(data: list[dict[str, str | float]]) -> list[dict[str, str | float]]:
    """
    Функция сортирует данные по выручке жанров.

    Args:
        data (list[dict[str, str | float]]): Список словарей, где каждый словарь содержит
            информацию о категории и выручке.

    Returns:
        list[dict[str, str | float]]: Отсортированный список по убыванию выручки.
    """
    return sorted(data, key=lambda item: item["total_sales"], reverse=True)

print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")

test_data_1 = [
    {"category": "Action", "total_sales": 4311.85},
    {"category": "Animation", "total_sales": 4656.30},
    {"category": "Children", "total_sales": 3655.55},
]

print("\n--- ТЕСТ 1 ---")
sorted_report = get_sorted_report(test_data_1)
print("Топ категорий по выручке:")
for number, item in enumerate(sorted_report, 1):
    print(f"{number}. {item['category']}: {item['total_sales']}")

test_data_2 = [
    {"category": "Classics", "total_sales": 1200.10},
    {"category": "Comedy", "total_sales": 4000.00},
    {"category": "Documentary", "total_sales": 4000.00},
]

print("\n--- ТЕСТ 2 ---")
sorted_report = get_sorted_report(test_data_2)
print("Топ категорий по выручке:")
for number, item in enumerate(sorted_report, 1):
    print(f"{number}. {item['category']}: {item['total_sales']}")

test_data_3 = [
    {"category": "Drama", "total_sales": 500.00},
]

print("\n--- ТЕСТ 3 ---")
sorted_report = get_sorted_report(test_data_3)
print("Топ категорий по выручке:")
for number, item in enumerate(sorted_report, 1):
    print(f"{number}. {item['category']}: {item['total_sales']}")
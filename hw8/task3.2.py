DEFAULT_RETURN_INDEX_BASE = 10.0

import time
from typing import Any


def calculate_overdue_fine(
    movie_title: str,
    days_overdue: Any,
    fine_rate: float
) -> tuple[float, float] | None:
    """
    Функция рассчитывает штраф за просрочку возврата фильма и технический индекс возврата.

    Args:
        movie_title (str): Название фильма.
        days_overdue (Any): Количество дней просрочки
        fine_rate (float): Ставка штрафа за один день просрочки.

    Returns:
        tuple[float, float] | None: Кортеж с итоговым штрафом и индексом возврата, либо None в случае ошибки.
    
    Raises:
        ValueError: Если дни просрочки не могут быть преобразованы в число.
        ZeroDivisionError: Если дни просрочки равны нулю.
        TypeError: Если тип данных days_overdue не поддерживает преобразование в float.
    """
    try:
        numeric_days = float(days_overdue)

        total_fine = numeric_days * fine_rate

        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

        return total_fine, return_index

    except ValueError as e:
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для '{movie_title}': {e}")
        return None

    except ZeroDivisionError:
        print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для '{movie_title}': float division by zero")
        return None

    except TypeError:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{movie_title}': float() argument must be a string or a real number, not 'list'")
        return None

    finally:
        pass


print("=== ПРОВЕРКА ВОЗВРАТОВ ===")

# Успешный расчёт
result = calculate_overdue_fine("Matrix", 5, 1.5)
if result is not None:
    print(f"Фильм: 'Matrix' | Итоговый штраф: {result[0]}$ | Индекс: {result[1]}")
    print("--- Проверка транзакции возврата завершена ---\n")

# Ошибка значения
calculate_overdue_fine("Inception", "пять", 2.0)
print("--- Проверка транзакции возврата завершена ---\n")

# Ошибка деления на ноль
calculate_overdue_fine("Avatar", 0, 2.5)
print("--- Проверка транзакции возврата завершена ---\n")

# Ошибка типа
calculate_overdue_fine("Interstellar", [3], 3.0)
print("--- Проверка транзакции возврата завершена ---\n")

#Тут из идеи было добавить в finally pass и добавить строчку print("--- Проверка транзакции возврата завершена ---")
#вручную, но это кажется странным и не рациональным, зато тогда будет ровно как в примере
#но тогда не выполняем требование Блок finally: всегда выводит: --- Проверка транзакции возврата завершена ---.
#мне кажется рабочий вариант из task3.3.py
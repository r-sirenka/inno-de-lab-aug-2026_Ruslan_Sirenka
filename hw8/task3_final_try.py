DEFAULT_RETURN_INDEX_BASE = 10.0

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

    Note:
        Функция обрабатывает следующие ошибки и возвращает None:
        - ValueError: Если дни просрочки не могут быть преобразованы в число.
        - ZeroDivisionError: Если дни просрочки равны нулю.
        - TypeError: Если тип данных days_overdue не поддерживает преобразование в float.
    """
    try:
        numeric_days = float(days_overdue)
        total_fine = numeric_days * fine_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

    except ValueError as e:
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для '{movie_title}': {e}\n")
        return None

    except ZeroDivisionError as e:
        print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для '{movie_title}': {e}\n")
        return None

    except TypeError as e:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{movie_title}': {e}\n")
        return None

    else:
        print(f"Фильм: '{movie_title}' | Итоговый штраф: {total_fine}$ | Индекс: {return_index}\n")
        return total_fine, return_index
    #вариант с блоком else, если соблюдать, что в try могут быть только 3 действия
    #как по мне самый правильный и рабочий

    finally:
        print("--- Проверка транзакции возврата завершена ---\n")


print("=== ПРОВЕРКА ВОЗВРАТОВ ===\n")

calculate_overdue_fine("Matrix", 5, 1.5)
calculate_overdue_fine("Inception", "пять", 2.0)
calculate_overdue_fine("Avatar", 0, 2.5)
calculate_overdue_fine("Interstellar", [3], 3.0)
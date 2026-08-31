MAX_RENTAL_BATCH_LIMIT = 150.0

def calculate_rental_batch(
    quantity: int,
    rental_rate: float,
    discount: float = 0.0
) -> tuple[float, bool]:
    """
    Функция рассчитывает итоговую стоимость партии дисков и проверяет превышение лимита.

    Args:
        quantity (int): Количество дисков в партии.
        rental_rate (float): Цена за один диск.
        discount (float): Скидка в процентах (по умолчанию 0.0).

    Returns:
        tuple[float, bool]: Кортеж, содержащий итоговую сумму и превышения лимита.
    """
    final_sum = round(quantity * rental_rate * (1 - discount), 2)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT
    return final_sum, is_limit_exceeded

print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")

result = calculate_rental_batch(30, 2.99)
print(f"Партия 1 (Academy Dinosaur): Сумма {result[0]}$. Превышение лимита: {result[1]}")

result = calculate_rental_batch(40, 4.99, 0.1)
print(f"Партия 2 (Affair Prejudice): Сумма {result[0]}$. Превышение лимита: {result[1]}")

result = calculate_rental_batch(10, 1.99)
print(f"Партия 3 (Agent Truman): Сумма {result[0]}$. Превышение лимита: {result[1]}")

result = calculate_rental_batch(50, 3.50, 0.2)
print(f"Партия 4 (African Egg): Сумма {result[0]}$. Превышение лимита: {result[1]}")
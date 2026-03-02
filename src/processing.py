"""
Модуль с функциями для обработки данных банковских операций.
Содержит функции для фильтрации и сортировки операций.
"""

from typing import List, Dict, Any


def filter_by_state(operations: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по значению ключа 'state'.

    Параметры:
    - operations: список словарей с данными об операциях
    - state: значение для фильтрации (по умолчанию 'EXECUTED')

    Возвращает:
    - Новый список, содержащий только операции с указанным state
    """
    return [operation for operation in operations if operation.get('state') == state]


def sort_by_date(operations: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по дате.

    Параметры:
    - operations: список словарей с данными об операциях
    - reverse: True для сортировки по убыванию (сначала новые),
               False для сортировки по возрастанию (сначала старые)

    Возвращает:
    - Новый отсортированный список операций
    """
    sorted_operations = operations.copy()
    sorted_operations.sort(key=lambda x: x['date'], reverse=reverse)
    return sorted_operations


if __name__ == "__main__":
    # Тестовые данные из задания
    test_data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    print("=" * 50)
    print("ТЕСТИРОВАНИЕ ФУНКЦИЙ ОБРАБОТКИ")
    print("=" * 50)

    # Тест filter_by_state
    print("\n1. filter_by_state (EXECUTED):")
    print(filter_by_state(test_data))

    print("\n2. filter_by_state (CANCELED):")
    print(filter_by_state(test_data, 'CANCELED'))

    # Тест sort_by_date
    print("\n3. sort_by_date (по убыванию):")
    print(sort_by_date(test_data))

    print("\n4. sort_by_date (по возрастанию):")
    print(sort_by_date(test_data, reverse=False))

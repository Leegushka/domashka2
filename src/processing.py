"""
Модуль с функциями для обработки данных банковских операций.

Содержит функции:
- filter_by_state: фильтрация операций по статусу
- sort_by_date: сортировка операций по дате
"""

from typing import List, Dict, Any, Optional


def filter_by_state(operations: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по значению ключа 'state'.

    Параметры:
    - operations: список словарей с данными об операциях
    - state: значение для фильтрации (по умолчанию 'EXECUTED')

    Возвращает:
    - Новый список, содержащий только операции с указанным state

    Пример:
    >>> data = [{'id': 1, 'state': 'EXECUTED'}, {'id': 2, 'state': 'CANCELED'}]
    >>> filter_by_state(data)
    [{'id': 1, 'state': 'EXECUTED'}]
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

    Пример:
    >>> data = [{'date': '2023-01-01'}, {'date': '2022-01-01'}]
    >>> sort_by_date(data)
    [{'date': '2023-01-01'}, {'date': '2022-01-01'}]
    """
    # Создаем копию списка, чтобы не изменять исходный
    sorted_operations = operations.copy()

    # Сортируем по ключу 'date'
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
    print("ТЕСТИРОВАНИЕ ФУНКЦИЙ")
    print("=" * 50)

    # Тест filter_by_state со статусом по умолчанию
    print("\n1. filter_by_state (по умолчанию 'EXECUTED'):")
    result1 = filter_by_state(test_data)
    for item in result1:
        print(f"   {item}")

    # Тест filter_by_state с 'CANCELED'
    print("\n2. filter_by_state (state='CANCELED'):")
    result2 = filter_by_state(test_data, 'CANCELED')
    for item in result2:
        print(f"   {item}")

    # Тест sort_by_date (по умолчанию - убывание)
    print("\n3. sort_by_date (по умолчанию - убывание):")
    result3 = sort_by_date(test_data)
    for item in result3:
        print(f"   {item['date']} - {item['state']}")

    # Тест sort_by_date (возрастание)
    print("\n4. sort_by_date (reverse=False - возрастание):")
    result4 = sort_by_date(test_data, reverse=False)
    for item in result4:
        print(f"   {item['date']} - {item['state']}")
from typing import Any


def filter_by_state(transactions_list: list[dict[str, Any]], state: str = "EXECUTED") -> list:
    """Функция для отслеживания статуса"""
    state_filter = []
    for item in transactions_list:
        if item["state"] == state:
            state_filter.append(item)
    return state_filter


def sort_by_date(transactions_list: list[dict[str, Any]], desc: bool = True) -> list:
    """Функция для сортировки по дате"""
    return sorted(transactions_list, key=lambda item: item["date"], reverse=desc)

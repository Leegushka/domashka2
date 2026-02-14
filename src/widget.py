from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счёта.
    """
    if info.startswith("Счет"):
        return f"Счет {get_mask_account(info)}"
    return f"{info.rsplit(' ', 1)[0]} {get_mask_card_number(info)}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата '2024-03-11T02:26:18.671407'
    в формат '11.03.2024'.
    """
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")

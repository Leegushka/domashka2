def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты: оставляет первые 6 и последние 4 цифры,
    остальные заменяет на звёздочки.
    Пример: 7000792289606361 -> 7000 79** **** 6361
    """
    masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked


def get_mask_account(account_info: str) -> str:
    """
    Маскирует номер счёта: оставляет только последние 4 цифры,
    остальные заменяет на **.
    Пример: 73654108430135874305 -> **4305
    """
    account_number = account_info.split()[-1]
    return f"**{account_number[-4:]}"

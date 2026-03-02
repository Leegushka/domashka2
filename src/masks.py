def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.
    Формат: XXXX XX** **** XXXX
    """
    if len(card_number) < 16:
        return "Недостаточно цифр"

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета.
    Формат: **XXXX
    """
    if len(account_number) < 4:
        return "Недостаточно цифр"

    return f"**{account_number[-4:]}"


if __name__ == "__main__":
    # Простое тестирование
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))


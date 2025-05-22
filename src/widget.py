from masks import get_mask_account, get_mask_card_number


def mask_account_card(information: str) -> str:
    """Функция маскировки номера банковской карты/счета"""
    number = information.split(" ")[-1]
    if len(number) == 16:
        return f"{' '.join(information.split(' ')[0:-1])} {get_mask_card_number(number)}"
    elif len(number) == 20:
        return f"{' '.join(information.split(' ')[0:-1])} {get_mask_account(number)})"
    else:
        return "Некорректный номер карты/счета"

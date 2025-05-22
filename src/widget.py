from masks import get_mask_card_number, get_mask_account


def mask_account_card(information: str) -> str:
    """Функция маскировки номера банковской карты/счета"""
    items = information.split(" ")
    mask_number = []
    for i in items:
        if i.isdigit() and (len(i) == 16):
            mask_number.append(get_mask_card_number(i))
        elif i.isdigit() and (len(i) == 20):
            mask_number.append(get_mask_account(i))
        elif i.isalpha():
            mask_number.append(i)
        else:
            return "Некорректный номер карты/счета"

    return " ".join(mask_number)
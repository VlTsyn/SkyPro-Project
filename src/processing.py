def filter_by_state(transactions_list: list, state: str = "EXECUTED") -> list:
    state_filter = []
    for item in transactions_list:
        if item["state"] == state:
            state_filter.append(item)
    return state_filter


def sort_by_date(transactions_list: list, desc: bool = True) -> list:
    return sorted(transactions_list, key=lambda item: item["date"], reverse=desc)

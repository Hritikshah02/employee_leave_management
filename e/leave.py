def check_leave(balance, requested):
    if requested <= 0:
        raise ValueError("Invalid leave request")
    return requested <= balance

def validate(balance, days):
    return 0 < days <= balance

assert validate(10, 3)
assert not validate(2, 5)
assert not validate(5, 0)
print("Leave balance validation passed")

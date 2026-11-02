import pytest
from leave import check_leave

@pytest.mark.parametrize("balance, requested, expected", [
    (10, 5, True),    # valid
    (10, 10, True),   # valid (exact)
    (3, 5, False),    # insufficient
])
def test_check_leave(balance, requested, expected):
    assert check_leave(balance, requested) == expected

@pytest.mark.parametrize("requested", [0, -2])  # zero, invalid
def test_invalid_leave(requested):
    with pytest.raises(ValueError):
        check_leave(10, requested)

# ---------------- STEPS (e) ----------------
# 1. Cases: valid (10,5), valid exact (10,10), insufficient (3,5), zero (0), invalid (-2)
# 2. Use @pytest.mark.parametrize for multiple inputs
# 3. Use assert / pytest.raises to verify results
# 4. Run: pytest -v   -> 5 passed

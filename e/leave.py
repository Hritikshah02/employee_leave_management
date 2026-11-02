def check_leave(balance, requested):
    if requested <= 0:
        raise ValueError("Invalid leave request")
    return requested <= balance

# ---------------- STEPS (e) Automated Testing Using PyTest ----------------
# 1. Write check_leave() in leave.py
# 2. Write test_leave.py with @pytest.mark.parametrize + assert
# 3. pip install pytest
# 4. cd e && pytest -v

def validate(balance, days):
    return 0 < days <= balance

assert validate(10, 3)
assert not validate(2, 5)
assert not validate(5, 0)
print("Leave balance validation passed")

# ---------------- STEPS (b) CI/CD Using GitHub Actions ----------------
# 1. Write this validation script (b/leave_balance.py)
# 2. Create .github/workflows/ci.yml at repo root (trigger: push to main)
#    -> checkout, setup-python, run: python b/leave_balance.py
# 3. git add . && git commit -m "Add leave balance CI"
# 4. git remote add origin <repo-url> && git push -u origin main
# 5. Open GitHub repo > Actions tab > see green run and log
#    "Leave balance validation passed"

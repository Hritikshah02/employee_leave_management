def apply_leave(balance, days):
    return balance - days

def leave_request(name, days):
    return f"{name} requested {days} days leave"

# ---------------- STEPS (a) Version Control Using Git ----------------
# 1. git init -b main
# 2. git add . && git commit -m "Initial leave app"
# 3. git checkout -b feature/leave-request
# 4. Add/modify leave_request() in leave.py
# 5. git add . && git commit -m "Add leave-request function"
# 6. git checkout main
# 7. git merge --no-ff feature/leave-request
# 8. git log --oneline --graph --all   (shows commit history)

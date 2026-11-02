FROM python:3.11-slim
WORKDIR /app
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]

# ---------------- STEPS (d) ----------------
# 1. docker build -t leave-app .
# 2. docker run -d --name leave-container -p 8080:5000 leave-app
# 3. docker ps
# 4. docker logs leave-container

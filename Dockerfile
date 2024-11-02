# Вказуємо базовий образ

FROM python:3.9

# Встановлюємо робочу директорію

WORKDIR /app

# Копіюємо файли проекту в контейнер

COPY . .

# Встановлюємо залежності

RUN pip install --no-cache-dir -r requirements.txt

# Вказуємо команду для запуску додатку

CMD ["python", "app.py"]

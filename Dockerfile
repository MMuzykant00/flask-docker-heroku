FROM python:3.11

# Ustawienie katalogu roboczego
WORKDIR /app

# Skopiowanie plików do obrazu
COPY . /app

# Instalacja zależności
RUN pip install --no-cache-dir -r requirments.txt

# Ustawienie zmiennej środowiskowej dla Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Eksponowanie portu aplikacji
EXPOSE 5000

# Uruchomienie aplikacji
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]

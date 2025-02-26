# Flask Docker App 🚀

Prosty projekt aplikacji Flask działającej w kontenerze Docker.

## 📌 Jak uruchomić aplikację

1. **Sklonuj repozytorium**
   ```sh
   git clone https://github.com/MMuzykant00/flask-docker-heroku.git
   cd flask-docker-heroku
   ```

2. **Zbuduj obraz Dockera**
   ```sh
   docker build -t flask-app .
   ```

3. **Uruchom kontener**
   ```sh
   docker run -d -p 5000:5000 --name flask-container flask-app
   ```

4. **Sprawdź aplikację**
   Otwórz w przeglądarce:
   ```
   http://localhost:5000/hello
   ```

## 🔥 Zarządzanie kontenerem
- **Zatrzymanie kontenera:**
  ```sh
  docker stop flask-container
  ```
- **Usunięcie kontenera:**
  ```sh
  docker rm flask-container
  ```
- **Usunięcie obrazu:**
  ```sh
  docker rmi flask-app
  ```

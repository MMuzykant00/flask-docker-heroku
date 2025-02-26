# Flask Docker App 🚀

A simple Flask web application running inside a Docker container. This project provides a basic example of how to deploy a Flask application using Docker and is ready for deployment on Heroku or Render.

![Demo GIF](gif/Presentation.gif)

## 📌 How to Run the Application

1. **Clone the repository**
   ```sh
   git clone https://github.com/MMuzykant00/flask-docker-heroku.git
   cd flask-docker-heroku
   ```

2. **Build the Docker image**
   ```sh
   docker build -t flask-app .
   ```

3. **Run the container**
   ```sh
   docker run -d -p 5000:5000 --name flask-container flask-app
   ```

4. **Check the application**
   Open your browser and visit:
   ```
   http://localhost:5000/hello
   ```

## 🔥 Managing the Container
- **Stop the container:**
  ```sh
  docker stop flask-container
  ```
- **Remove the container:**
  ```sh
  docker rm flask-container
  ```
- **Remove the Docker image:**
  ```sh
  docker rmi flask-app
  ```



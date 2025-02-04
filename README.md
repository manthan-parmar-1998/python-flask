# Python Flask Application

A simple Flask web application containerized with Docker and Docker Compose.

## Features

-   Basic Flask web server with two endpoints
-   Docker containerization
-   Docker Compose support
-   Lightweight Python slim base image
-   Auto-reload in development mode

## Project Structure

```
flask-app/
├── app/
│   ├── app.py          # Flask application code
│   └── Dockerfile      # Docker configuration
├── docker-compose.yml  # Docker Compose configuration
└── README.md           # This documentation
```

## Prerequisites

-   Docker Engine (version 19.03+)
-   Docker Compose (version 1.27+)
-   Git (optional)

## Getting Started

### Using Docker Compose (Recommended)

```bash
# Start the application
docker-compose up

# Run in detached mode
docker-compose up -d

# Stop the application
docker-compose down
```

### Manual Docker Build

```bash
# Build the Docker image
docker build -t flask-app ./app

# Run the container
docker run -p 5000:5000 flask-app

# Run in detached mode
docker run -d -p 5000:5000 --name my-flask-app flask-app
```

## Application Endpoints

-   Home page: http://localhost:5000
-   About page: http://localhost:5000/about

## Configuration

-   **Port:** 5000 (modify in `docker-compose.yml` if needed)
-   **Environment:** Development (debug mode enabled)
-   **Base Image:** Python 3.12 slim

## Managing Containers

```bash
# List running containers
docker ps

# Stop a container
docker stop <container-id>

# View container logs
docker logs <container-id>

# Remove all stopped containers
docker container prune
```

## Development

1. Clone the repository:

```bash
git clone https://github.com/manthan-parmar-1998/python-flask.git
```

2. Navigate to project directory:

```bash
cd python-flask
```

3. Follow the [Getting Started](#getting-started) instructions

## Important Notes

-   Debug mode is enabled (not suitable for production)
-   Application listens on all interfaces (`0.0.0.0`)
-   Container includes Flask 2.0.1
-   Docker image uses Python 3.8 slim base image

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

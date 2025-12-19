# LLM Server using Ollama, Docker, and FastAPI

This project sets up a local LLM (Large Language Model) server using Ollama running in Docker, with a FastAPI application to provide an API interface for interacting with the model.

## Overview

- **Ollama**: Runs the LLM models in a Docker container.
- **FastAPI**: Provides a REST API to send prompts to the Ollama server and receive responses.
- **Docker Compose**: Manages the services (Ollama and the FastAPI app).

The setup ensures that the FastAPI app communicates with Ollama inside the Docker network.

## Prerequisites

- Docker and Docker Compose installed.
- Postman or any API testing tool (optional, for testing).

## Running the Server
  docker-compose up --build
  Send a POST request to http://localhost:8000/chat

## Experiences and Lessons Learned
- Remember the stack: Docker + FastAPI + Ollama.
- Do not access LLM directly from the host machine; models are pulled inside the container.
- Common issue: Wrong model version – ensure the pulled model matches (e.g., llama3.2:latest).
- Environment: Use the Docker service name (ollama) for OLLAMA_URL, not localhost/127.0.0.1.
- Testing: Use Postman to send JSON payloads and inspect network requests/responses.

## Troubleshooting
- If model not found: Re-pull inside the container.
    docker exec -it ollama ollama pull llama3.2:latest
- Connection issues: Verify service names and network in Docker Compose.

## Furture work

### 1. Request/Response Logging System
Implement comprehensive logging for all incoming requests and LLM responses:
- Log timestamp, user prompt, model used, full response, response time, and any errors.
- Store logs in structured format (JSON) for easy querying.
- Options:
  - Simple file-based logging (e.g., rotating JSON logs).
  - Integrate with a database.

### 2. Response Tuning Based on User Feedback
- Add a feedback mechanism to improve future responses:
- Add a /feedback endpoint where users submit thumbs up/down or comments on a specific response (include a response ID from logs).
- Store feedback in the database.
Future: Use feedback data for:
- Fine-tuning lighter models (via LoRA or similar).
- Prompt engineering adjustments.
- Simple retrieval of highly-rated past responses for similar prompts.

### 3. Multi-Model Docker Setup
- Support multiple lightweight LLMs for different use cases.

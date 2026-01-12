# CryptoStream Architect

Real-time cryptocurrency analytics service. The system ingests trade data from Binance WebSocket API, calculates technical indicators (SMA) in real-time using Redis Streams, and persists aggregated data to PostgreSQL.

## Architecture

The system follows a microservice-like architecture within a modular monolith structure:

1.  **Ingestion Service:** Connects to Binance WebSocket, normalizes raw trade data, and pushes it to Redis Streams.
2.  **Analytics Worker:** Consumes data from Redis, calculates moving averages, detects trends, and stores aggregated candles (1-minute intervals) in PostgreSQL.
3.  **API Gateway:** FastAPI application providing REST endpoints for historical data and WebSocket endpoints for real-time client updates.

## Technology StackS

* **Language:** Python 3.11+
* **Web Framework:** FastAPI
* **Database:** PostgreSQL (Async via SQLAlchemy 2.0 + asyncpg)
* **Message Broker / Cache:** Redis (Streams & Pub/Sub)
* **Migration Tool:** Alembic
* **Containerization:** Docker & Docker Compose

## Prerequisites

* Docker Engine & Docker Compose
* Python 3.11+ (for local development)

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/dauzhaa/TradeWatcher
    cd cryptostream
    ```

2.  Create a virtual environment and install dependencies:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/MacOS
    # .venv\Scripts\activate   # Windows
    pip install -r requirements.txt
    ```

3.  Configure environment variables:
    Create a `.env` file in the root directory:
    ```ini
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_DB=cryptostream
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432
    
    REDIS_HOST=localhost
    REDIS_PORT=6379
    ```

## Running the Application

### Infrastructure (Database & Redis)
Start the required services using Docker:
```bash
docker-compose up -d redis db
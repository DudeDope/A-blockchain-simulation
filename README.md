
# 🧱 Dockerized Blockchain Simulation

This project simulates a basic blockchain with a **Flask** backend and **React** frontend, all running in Docker containers. The system includes core blockchain concepts like block creation, mining (proof-of-work), and transaction management. It demonstrates how to use Docker to containerize a full-stack web application.

---

## 📦 Features

- **Backend** (Flask):
  - Create a blockchain
  - Add transactions
  - Mine blocks using proof-of-work
  - Expose an API to interact with the blockchain
- **Frontend** (React):
  - View the entire blockchain
  - Add new transactions
  - Mine new blocks via the UI
- **Dockerized**:
  - Backend and frontend are each in their own containers
  - Use `docker-compose` to link them together

---

## 🖥️ Requirements

- **Docker**: Docker Engine installed and running.
- **Docker Compose**: Ensure you have Docker Compose installed.

---

## 🚀 Setup & Execution Instructions

### 1. Clone or Download This Repository

```bash
git clone https://github.com/your-username/simple-blockchain-docker.git
cd simple-blockchain-docker
```

---

### 2. Build and Run the Containers

Run the following command to build and start the application:

```bash
docker-compose up --build
```

- **Backend** will run on [http://localhost:5000](http://localhost:5000)
- **Frontend** will run on [http://localhost](http://localhost)

---

## 🧠 Code Overview

### 📦 `blockchain.py` (Backend)

- **`Block` class**: Defines the structure of a block in the blockchain, including methods for hash calculation and tampering prevention.
- **`Blockchain` class**: Handles the creation and management of the blockchain, including adding transactions, mining blocks, and validating the chain.

### 🔗 `app.py` (Backend)

- Exposes RESTful API endpoints:
  - `GET /chain`: Returns the current blockchain.
  - `POST /transaction`: Adds a new transaction.
  - `POST /mine`: Mines a new block with pending transactions.

### 🖼️ `App.js` (Frontend)

- React-based interface to interact with the blockchain:
  - Displays the entire blockchain.
  - Allows users to add new transactions.
  - Provides a button to mine new blocks.

### 🗂️ Docker Setup

- **Dockerfile (Backend)**: Sets up a Flask server to run the backend.
- **Dockerfile (Frontend)**: Builds and serves the React app using Nginx.
- **docker-compose.yml**: Links the backend and frontend containers, ensuring communication between them on a custom network.

---

## 🔍 Example Output

```bash
Mining Block #1...
Block #1 mined: 000ac9d0f...

Mining Block #2...
Block #2 mined: 000bba4b8...

=== Validating Blockchain ===
Is chain valid? True

=== Tampering with Blockchain ===
Tampering with Block #1...
Is chain valid? False
```

---

## 📚 Learning Objectives

- Learn about **blockchain basics** like blocks, transactions, and mining.
- Understand how to **containerize applications** using Docker and Docker Compose.
- Experience **frontend-backend communication** in a full-stack setup.
- Experiment with the **proof-of-work** concept used in real-world blockchains like Bitcoin.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ✍️ Author

Developed by [Your Name]


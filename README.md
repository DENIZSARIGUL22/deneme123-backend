# deneme123-backend

A Flask-based backend API for the E-Vote Android app, providing JWT-secured endpoints for registration, login, voting, and result retrieval.

---

## Table of Contents

- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Setup & Run](#setup--run)  
- [API Reference](#api-reference)  
- [Contributing](#contributing)  
- [License](#license)  

---

## 🚀 Features

- **User Authentication** – `/auth/register`, `/auth/login` with JWT tokens  
- **Vote Casting** – `/vote` endpoint enforces one-vote-per-user policy  
- **Results Retrieval** – `/results` returns live vote tallies  
- **Candidate Management** – protected `/candidates` CRUD (admin only)  
- **Announcements & Feedback** – `/updates` for council news, `/feedback` to receive messages  

---

## 🏗 Tech Stack

- **Python** 3.9+  
- **Flask** (Flask-JWT-Extended, Flask-Migrate, Flask-CORS)  
- **SQLAlchemy** ORM (SQLite/MySQL)  
- **Alembic** migrations  
- **JWT** for stateless auth  

---

## 🎬 Getting Started

### Prerequisites

- Python 3.9 or higher  
- pip  

### Setup & Run

```bash
# 1. Clone repository
git clone https://github.com/DENIZSARIGUL22/deneme123-backend.git
cd deneme123-backend

# 2. Create & activate virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
# source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Initialize database
flask db upgrade

# 5. Run development server
flask run --host=0.0.0.0 --port=5000
Base URL: http://localhost:5000/

🔌 API Reference
Method	Endpoint	Auth	Description
POST	/auth/register	–	Create a new user
POST	/auth/login	–	Authenticate & receive JWT
GET	/auth/me	JWT	Retrieve current user info
POST	/vote	JWT	Cast a vote
GET	/results	JWT	Get live vote tallies
GET	/candidates	JWT/admin	List all candidates
POST	/candidates	JWT/admin	Add a new candidate
PUT	/candidates/<id>	JWT/admin	Update candidate details
DELETE	/candidates/<id>	JWT/admin	Remove a candidate
GET	/updates	–	List council announcements
POST	/feedback	–	Submit feedback message

🤝 Contributing
Fork & clone this repo

Create a feature branch:

bash

git checkout -b feat/YourFeature
Commit your changes with clear messages

Push & open a Pull Request

📜 License
This project is licensed under the MIT License.



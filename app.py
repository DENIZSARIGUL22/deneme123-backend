# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.security import check_password_hash
import mysql.connector

app = Flask(__name__)
CORS(app)

# MySQL bağlantısı
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",        # phpMyAdmin parolanız (boşsa "")
    database="evote_db" # Oluşturduğunuz veritabanı
)

# 1) Health-check endpoint
@app.route("/ping", methods=["GET"])
def ping():
    return "pong", 200

# 2) Login endpoint
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    email = data.get("email", "")
    password = data.get("password", "")

    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT password_hash FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()

    if not user:
        return jsonify(success=False, message="Kullanıcı bulunamadı"), 404

    if check_password_hash(user["password_hash"], password):
        return jsonify(success=True, token="demo-token-123"), 200
    else:
        return jsonify(success=False, message="Şifre yanlış"), 401

# 3) GET /candidates — Aday listesi
@app.route("/candidates", methods=["GET"])
def get_candidates():
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT
            id,
            name,
            department,
            bio,
            photo_url AS photoUrl
        FROM candidates
    """)
    rows = cursor.fetchall()
    return jsonify(rows), 200

# 4) POST /vote — Oy kullanma endpoint’i
@app.route("/vote", methods=["POST"])
def vote():
    data = request.get_json() or {}
    candidate_id = data.get("candidateId")
    token = request.headers.get("Authorization", "").replace("Bearer ", "")

    # Basit demo token doğrulaması
    if token != "demo-token-123":
        return jsonify(success=False, message="Yetkilendirme hatası"), 401

    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO votes (candidate_id) VALUES (%s)",
        (candidate_id,)
    )
    db.commit()
    return jsonify(success=True), 200

# 5) GET /results — Oy sonuçları endpoint’i
@app.route("/results", methods=["GET"])
def results():
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT
            c.id,
            c.name,
            COUNT(v.id) AS votes
        FROM candidates c
        LEFT JOIN votes v ON v.candidate_id = c.id
        GROUP BY c.id, c.name
        ORDER BY c.id
    """)
    rows = cursor.fetchall()
    return jsonify(rows), 200

# 6) GET /announcements — Duyuru listesi endpoint’i
@app.route("/announcements", methods=["GET"])
def get_announcements():
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT
            id,
            message
        FROM announcements
        ORDER BY created_at DESC
    """)
    rows = cursor.fetchall()
    return jsonify(rows), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  
from flask import Flask, request, jsonify, render_template
import requests
from dotenv import load_dotenv
import os
from gigachat import GigaChat

# Загрузка переменных окружения
load_dotenv()

app = Flask(__name__)

# Настройка GigaChat API
GIGACHAT_API_URL = "https://gigachat.devices.sberbank.ru/api/v1/models"  # 
GIGACHAT_API_KEY = os.getenv("GIGACHAT_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    # Запрос к GigaChat API
    headers = {
        "Authorization": f"Bearer {GIGACHAT_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "GigaChat",  # Уточнить название модели 
        "scope": "GIGACHAT_API_PERS",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 100,
        "temperature": 0.7,
    }

    try:
        response = requests.post(GIGACHAT_API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Проверка на ошибки
        result = response.json()

        # Возврат ответа
        return jsonify({"response": result["choices"][0]["message"]["content"]})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
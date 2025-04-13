from flask import Flask, request, jsonify, render_template
import traceback
from model import get_model_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    # Запрос к GigaChat API
    try:
        response = get_model_response(prompt)
        return jsonify({"response": response})
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500
        

if __name__ == "__main__":
    app.run(debug=True)
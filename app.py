from flask import Flask, request, jsonify
from telestrations import Telestrations
import os
from dotenv import load_dotenv

app = Flask(__name__, static_folder="static", static_url_path="")
load_dotenv()

openai_api_key = os.environ.get("OPENAI_API_KEY")

svc = Telestrations()

@app.post("/api/gen-image")
def gen_image():
    return jsonify({"url": svc.get_image_url_from_prompt(request.json["prompt"])})

@app.post("/api/gen-prompt")
def gen_prompt():
    return jsonify({"prompt": svc.get_prompt_from_image(request.json["image"])})

if __name__ == "__main__":
    app.run(debug=True)

@app.get("/")
def home():
    return app.send_static_file("index.html")
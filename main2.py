from flask import Flask, request
from google import genai

client = genai.Client(api_key="AIzaSyBF6oeJWCovxLK31RN-gMOF2oB2a8SEUjU")

app = Flask(__name__)

@app.route("/")
def heome():
    return "OK"

@app.route("/chat", methods=["POST"])
def chat():
    return client.models.generate_content(
        model="gemini-2.5-flash",
        contents=request.json["msg"]
    ).text

app.run(port=5001)
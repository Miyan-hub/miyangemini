from flask import *

import os, requests

import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyBYO8bvnvgPQ3w4hYS2C4xFOpS2-sBDT94")

generation_config = {
  "temperature": 1,
  "top_p": 1,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain"
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config
)

chat_session = model.start_chat(
  history=[
  ]
)

@app.route("/")
def gemini():
    try:
        text = request.args.get('')
        if text == '':
            return "Please Fill With Text..."
        response = chat_session.send_message(text)
        return response.text, 200
    except:
        return "Error"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
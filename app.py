from flask import Flask, request, jsonify
from whisper_utils import transcribe_audio
from llm_utils import generate_response
from tts_utils import speak_response
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    audio = request.files['audio']
    audio_path = os.path.join("audio", audio.filename)
    audio.save(audio_path)

    user_text = transcribe_audio(audio_path)
    response = generate_response(user_text)
    audio_response_path = speak_response(response)

    return jsonify({"user_text": user_text, "response": response, "audio_response": audio_response_path})

if __name__ == "__main__":
    app.run(debug=True)

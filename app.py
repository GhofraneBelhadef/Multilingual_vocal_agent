from flask import Flask, request, jsonify, send_from_directory, send_file
from whisper_utils import transcribe_audio
from llm_utils import generate_response
from tts_utils import speak_response
from flask_cors import CORS
import os
import uuid

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    audio = request.files.get('audio')
    if audio is None:
        return jsonify({"error": "No audio file provided"}), 400

    # Génère un nom unique pour chaque fichier audio reçu
    filename = f"{uuid.uuid4()}.webm"

    if not os.path.exists("audio"):
        os.makedirs("audio")

    audio_path = os.path.join("audio", filename)
    audio.save(audio_path)

    # Transcription
    user_text = transcribe_audio(audio_path)

    # Génération de la réponse
    response = generate_response(user_text)

    # Synthèse vocale (retourne chemin du fichier audio généré)
    audio_response_path = speak_response(response)

    return jsonify({
        "user_text": user_text,
        "response": response,
        "audio_response": f"/audio/{os.path.basename(audio_response_path)}"
    })

@app.route('/audio/<filename>')
def serve_audio(filename):
    return send_from_directory('audio', filename)

@app.route('/')
def index():
    # Sert le fichier index.html situé dans le dossier static
    return send_file('static/index.html')

if __name__ == "__main__":
    app.run(debug=True)

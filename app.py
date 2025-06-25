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
    audio = request.files.get('audio')
    if audio is None:
        return jsonify({"error": "No audio file provided"}), 400

    filename = audio.filename
    print(f"filename = '{filename}'")

    # Si filename est vide ou None, donne un nom par défaut
    if not filename:
        filename = "default.wav"

    # Crée le dossier audio s'il n'existe pas
    if not os.path.exists("audio"):
        os.makedirs("audio")

    audio_path = os.path.join("audio", filename)
    print(f"audio_path = '{audio_path}'")

    # Sauvegarde le fichier audio
    audio.save(audio_path)

    # Transcription
    user_text = transcribe_audio(audio_path)

    # Génération de la réponse
    response = generate_response(user_text)

    # Synthèse vocale (retourne le chemin du fichier audio généré)
    audio_response_path = speak_response(response)

    return jsonify({"user_text": user_text, "response": response, "audio_response": audio_response_path})


if __name__ == "__main__":
    app.run(debug=True)

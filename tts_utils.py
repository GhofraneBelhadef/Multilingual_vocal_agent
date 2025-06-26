import pyttsx3
import os

def speak_response(text):
    if not os.path.exists('audio'):
        os.makedirs('audio')
    audio_path = 'audio/response.mp3'  # chemin où on sauvegarde

    engine = pyttsx3.init()
    engine.save_to_file(text, audio_path)
    engine.runAndWait()
    engine.stop()

    return f"/{audio_path}"  # Retourne le chemin relatif à la racine serveur

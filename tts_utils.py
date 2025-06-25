import pyttsx3

def speak_response(text):
    engine = pyttsx3.init()
    engine.save_to_file(text, "audio/response.mp3")
    engine.runAndWait()
    engine.stop()
    return 'audio/response.mp3'
    

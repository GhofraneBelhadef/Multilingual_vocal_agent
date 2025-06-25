from gpt4all import GPT4All

model = GPT4All("ggml-gpt4all-j-v1.3-groovy.bin", model_path="./models")

def generate_response(prompt):
    print("⏳ Génération en cours pour :", prompt)
    with model.chat_session():
        response = model.generate(prompt, max_tokens=20, temp=0.7, top_k=40)
    print("✅ Réponse générée.")
    return response

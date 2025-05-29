from transformers import pipeline

# Generate legal advice using Llama (simulated with OPT-350m)
def generate_legal_advice(query, language="en"):
    generator = pipeline("text-generation", model="facebook/opt-350m")  # Llama placeholder
    prompt = f"Provide legal advice in {language} for the query: {query}"
    advice = generator(prompt, max_length=150, num_return_sequences=1)[0]["generated_text"]
    return advice

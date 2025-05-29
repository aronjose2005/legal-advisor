from legal_advisor import generate_legal_advice
from blockchain_case_management import store_case_data
from multilingual_processing import audio_to_text, translate_text

def main():
    # Process multilingual audio input
    audio_path = "path/to/legal_query_audio.wav"  # Placeholder
    language = "es"  # Example: Spanish input
    audio_text = audio_to_text(audio_path, language)
    print(f"Audio Transcript ({language}): {audio_text}")

    # Translate to English for processing
    english_text = translate_text(audio_text, target_language="en")
    print(f"Translated to English: {english_text}")

    # Generate legal advice
    advice = generate_legal_advice(english_text, language="en")
    print(f"Legal Advice: {advice}")

    # Store case data on blockchain
    case_id = "case_001"
    case_data = f"Query: {english_text}, Advice: {advice}"
    tx_hash = store_case_data(case_id, case_data)
    print(f"Case Stored on Blockchain, Transaction Hash: {tx_hash}")

if __name__ == "__main__":
    main()

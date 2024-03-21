from google.cloud import speech
from google.oauth2 import service_account

def speech_to_text(audio_file, language_code):
    credentials = service_account.Credentials.from_service_account_file(
        'google/api_connection.json'
    )
    client = speech.SpeechClient(credentials=credentials)

    with open(audio_file, "rb") as audio_file:
        content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        # sample_rate_hertz değeri buradan kaldırıldı
        language_code=language_code
    )

    response = client.recognize(config=config, audio=audio)
    return response.results[0].alternatives[0].transcript if response.results else ''

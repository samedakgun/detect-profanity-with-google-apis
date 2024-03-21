from google.cloud import translate_v2 as translate
from google.cloud import speech_v1p1beta1 as speech
from google.oauth2 import service_account


def detect_language_text(text):
    credentials = service_account.Credentials.from_service_account_file(
        'google/api_connection.json'
    )
    client = translate.Client(credentials=credentials)
    result = client.detect_language(text)
    return result['language']


def detect_language_audio(audio_file):
    credentials = service_account.Credentials.from_service_account_file(
        'google/api_connection.json'
    )
    client = speech.SpeechClient(credentials=credentials)

    with open(audio_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
    )

    response = client.recognize(config=config, audio=audio)
    language = response.results[0].language_code

    return language


if __name__ == "__main__":
    input_type = input("Giriş tipi (ses/metin): ")

    if input_type == "ses":
        audio_file = input("Ses dosyasının yolunu giriniz: ")
        language = detect_language_audio(audio_file)
        print(f"Ses dosyasının dili: {language}")
    elif input_type == "metin":
        text = input("Metni giriniz: ")
        language = detect_language_text(text)
        print(f"Metnin dili: {language}")
    else:
        print("Geçersiz giriş tipi.")

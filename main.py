# main.py
from google.speech_to_text import speech_to_text
from google.translate import translate_text
from src.predict_for_swear import load_model_and_vectorizer, predict_profanity
from google.hertz_correction import correct_hertz


def main():
    languages = {
        "ingilizce": "en-US",
        "ispanyolca": "es-ES",
        "fransızca": "fr-FR",
        "türkçe": "tr-TR",
        "italyanca": "it-IT",
        "arapça": "ar-SA",
        "almanca": "de-DE",
        "çince": "zh-CN",
    }

    model, vectorizer = load_model_and_vectorizer()

    input_type = input("Giriş tipi (ses/metin): ")

    if input_type == "ses":
        audio_file = input("Ses dosyasının yolunu giriniz: ")
        print("Lütfen aşağıdaki dillerden birini seçin:")
        for key in languages.keys():
            print(key)
        language_name = input("Dosyanın dilini giriniz: ")
        language_code = languages.get(language_name.lower(), "en-US")

        corrected_audio_file = correct_hertz(audio_file)  # Örneklenme hızını düzelt
        transcript = speech_to_text(corrected_audio_file, language_code)

        # Kullanıcının girdiği dil İngilizce değilse, çeviri yap
        if language_code != 'en-US':
            transcript = translate_text(transcript, 'en')

        is_profanity = predict_profanity(transcript, model, vectorizer)

        print(f"Metin: {transcript}")
        print("Küfür içeriyor." if is_profanity else "Küfür içermiyor.")

    elif input_type == "metin":
        text = input("Metni giriniz: ")
        # Burada dil tespiti yapılmıyor, varsayılan olarak İngilizce kabul ediliyor
        # Gerekiyorsa dil tespiti ve çeviri adımları eklenebilir
        is_profanity = predict_profanity(text, model, vectorizer)
        print("Küfür içeriyor." if is_profanity else "Küfür içermiyor.")

    else:
        print("Geçersiz giriş tipi.")


if __name__ == "__main__":
    main()

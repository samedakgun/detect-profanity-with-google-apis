import joblib


def load_model_and_vectorizer(model_path='models/model.joblib', vectorizer_path='models/vectorizer.joblib'):
    # Model ve vektörleştiriciyi yükler
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    return model, vectorizer


def predict_profanity(text, model, vectorizer):
    # Metni vektörleştirir ve tahmin yapar
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)
    return prediction[0]


def main():
    model, vectorizer = load_model_and_vectorizer()

    # Kullanıcıdan metin girdisi al
    user_input = input("Metni giriniz: ")

    # Küfür tahmini yap
    is_profanity = predict_profanity(user_input, model, vectorizer)

    # Sonucu ekrana yazdır
    if is_profanity:
        print("TRUE.")
    else:
        print("FALSE.")


if __name__ == '__main__':
    main()

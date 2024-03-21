import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.calibration import CalibratedClassifierCV
from sklearn.svm import LinearSVC
import joblib  # joblib doğrudan import edilmiş

def train_and_save_model(raw_data_path='data/raw/clean_data.csv', model_dir='models/'):
    # Veri okuma
    data = pd.read_csv(raw_data_path)
    texts = data['text'].astype(str)
    y = data['is_offensive']

    # Metni vektörleştirme
    vectorizer = CountVectorizer(stop_words='english', min_df=0.0001)
    X = vectorizer.fit_transform(texts)

    # Modeli eğitme
    model = LinearSVC(class_weight="balanced", dual=False, tol=1e-2, max_iter=100000)
    cclf = CalibratedClassifierCV(estimator=model)
    cclf.fit(X, y)

    # Modeli ve vektörleştiriciyi kaydetme
    vectorizer_path = model_dir + 'vectorizer.joblib'
    model_path = model_dir + 'model.joblib'
    joblib.dump(vectorizer, vectorizer_path)
    joblib.dump(cclf, model_path)

# Fonksiyon çağrısı
if __name__ == '__main__':
    train_and_save_model()

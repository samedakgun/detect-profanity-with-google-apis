import librosa
import noisereduce as nr
import soundfile as sf

def clean_audio(input_path, output_path):
    # Dosyayı librosa ile yükle
    data, rate = librosa.load(input_path, sr=None)
    # Gürültüyü azalt
    reduced_noise = nr.reduce_noise(y=data, sr=rate)
    # Temizlenmiş ses dosyasını kaydet
    sf.write(output_path, reduced_noise, rate, subtype='PCM_24')

from pydub import AudioSegment

def correct_hertz(audio_path, target_hertz=16000):
    sound = AudioSegment.from_file(audio_path)
    sound = sound.set_frame_rate(target_hertz)
    corrected_path = audio_path.replace(".wav", "_corrected.wav")
    sound.export(corrected_path, format="wav")
    return corrected_path

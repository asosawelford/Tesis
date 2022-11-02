import numpy as np
import librosa
from librosa import griffinlim
import soundfile as sf
import os

directory = r'datasets\amazon_polly\enrique'
for filename in os.scandir(directory):
    if filename.is_file():
        save_path = filename.path.split("\\")[-1]
        # print(save_path)
        file_path = filename.path
        y, sr = librosa.load(file_path)
        # Get the magnitude spectrogram
        S = np.abs(librosa.stft(y))
        # Invert using Griffin-Lim
        y_inv = librosa.griffinlim(S)

        sf.write(f'{save_path}_GL.wav', y_inv, sr, subtype='PCM_24')

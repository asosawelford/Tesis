import numpy as np
import librosa
from librosa import griffinlim
import soundfile as sf

file_path = r'datasets\microsoft_azure\es-AR-TomasNeural\es-AR-TomasNeural0.wav'
y, sr = librosa.load(file_path)
# Get the magnitude spectrogram
S = np.abs(librosa.stft(y))
# Invert using Griffin-Lim
y_inv = librosa.griffinlim(S)

sf.write('prueba_GL.wav', y_inv, sr, subtype='PCM_24')

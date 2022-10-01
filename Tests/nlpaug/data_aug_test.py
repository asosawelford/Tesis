import nlpaug.augmenter.audio as naa
import numpy as np
from nlpaug.util.audio.visualizer import AudioVisualizer
import librosa
import librosa.display as librosa_display
import matplotlib.pyplot as plt
import soundfile as sf

file_path = r'datasets\microsoft_azure\es-AR-TomasNeural\es-AR-TomasNeural0.wav'
data, sr = librosa.load(file_path)

# Pitch
# aug = naa.PitchAug(sampling_rate=sr,zone=(0., 1.), factor=(0,1))
# augmented_data = aug.augment(data)

# librosa_display.waveshow(data, sr=sr, alpha=0.5)
# librosa_display.waveshow(augmented_data[0], sr=sr, color='r', alpha=0.25)

# plt.tight_layout()
# plt.show()

# Speed
# aug = naa.SpeedAug(zone=(0., 1.),factor=(0.9,0.9))
# augmented_data = aug.augment(data)

aug = naa.VtlpAug(sampling_rate=sr, zone=(0.,1.), coverage=1,factor=(0.9, 1.1))
augmented_data = aug.augment(data)

# AudioVisualizer.freq_power('VTLP Augmenter', data, sr, augmented_data)

sf.write('prueba1.wav', augmented_data[0], sr, subtype='PCM_24')

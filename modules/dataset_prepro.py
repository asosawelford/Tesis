import os
import pydub
from pydub.silence import split_on_silence
from pydub import AudioSegment


# .mp3 to .wav function
def mp3_to_wav(audio_path):
    audio = AudioSegment.from_mp3(audio_path)
    audio = audio.set_channels(1)
    audio = audio.set_frame_rate(22050)
    export_path = audio_path.split(".")[0]
    audio.export(f"{export_path}.wav", format="wav")


# Audio volume normalization
def match_target_amplitude(aChunk, target_dBFS):
    change_in_dBFS = target_dBFS - aChunk.dBFS
    return aChunk.apply_gain(change_in_dBFS)


def split(audio_path):
    audio = AudioSegment.from_wav(audio_path)
    min_silence_len = 500  # Split if there´s N [ms] of silence
    silence_thresh = -40  # Silence threshold [dB]
    audio = pydub.effects.normalize(audio)

    chunks = split_on_silence(
        audio,
        min_silence_len=min_silence_len,
        silence_thresh=silence_thresh,
    )
    export_path = audio_path.split(".")[0].split("\\")[-1]
    # timestr = time.strftime("%Y%m%d_%H%M%S") # Today's Date
    for i, chunk in enumerate(chunks):
        # Optional: Discard based on lenght of resulting audio
        if min_seconds * 1000 < len(chunk) < max_seconds * 1000:
            chunk = match_target_amplitude(chunk, -22.0)
            chunk.export(f"{dir_path}/{export_path}_{str(i)}.wav", format="wav")

if __name__ == "__main__":
    min_seconds = 1
    max_seconds = 15

    audiofile_path = 'sabrina_loquendo.wav'
    dir_path = "datasets\\loquendo\\" + audiofile_path.split(".")[0]  # .wav directory
    # os.mkdir(dir_path)


    # mp3_to_wav(os.path.join(dir_path, audiofile_path))
    split(os.path.join(dir_path, audiofile_path.split(".")[0] + ".wav"))

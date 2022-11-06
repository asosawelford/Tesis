if __name__ == "__main__":
    import torch, torchaudio
    import IPython
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import speechaugs
    import pyaudio  
    import wave  

    audiopath = 'Tests/VTLP/00000.wav'
    ex_waveform, SR = torchaudio.load(audiopath)

    def play_wav(audiopath):
        #define stream chunk   
        chunk = 1024  

        #open a wav format music  
        f = wave.open(audiopath,"rb")  
        #instantiate PyAudio  
        p = pyaudio.PyAudio()  
        #open stream  
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                        channels = f.getnchannels(),  
                        rate = f.getframerate(),  
                        output = True)  
        #read data  
        data = f.readframes(chunk)  

        #play stream  
        while data:  
            stream.write(data)  
            data = f.readframes(chunk)  

        #stop stream  
        stream.stop_stream()  
        stream.close()  

        #close PyAudio  
        p.terminate()

    # play_wav(audiopath)
    MAX_DURATION = 10.
    import albumentations as A

    augmented11 = speechaugs.VTLP(p=1., sr=SR)(waveform=ex_waveform)['waveform']
    torchaudio.save('vtlp.wav', augmented11, SR)
    IPython.display.Audio('vtlp.wav')

    play_wav(augmented11)
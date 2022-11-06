"""
Checks inside a directory every .wav/mp3 file to see if its corrupted or not
"""

import os
import librosa
import audioread

def audio_corrupt_check(directory):
    """
    Checks inside a directory every .wav/mp3 file to see if its corrupted or not
    """
    # iterate over files in directory
    for filename in os.listdir(directory):
        subdir = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isdir(subdir):
            foldername=subdir.split(".")[0][-2:]
            for audioname in os.listdir(subdir):
                g = os.path.join(subdir, audioname)
                try:
                    audioread.audio_open(g)
                except:
                    print(g.split("\\")[-1] +": " +  "\\".join(g.split("\\")[-4:]))


                

if __name__ == "__main__":
    directory = r'subjective_test\webmushra\configs\resources'
    audio_corrupt_check(directory)
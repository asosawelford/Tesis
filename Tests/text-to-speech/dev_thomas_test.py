from text_to_speech import speak

"""
Text: String ? The text to be read.
Language: String ? The language (IETF language tag) to read the text in.
Slow: Boolean ? Reads text more slowly.
Save: Boolean ? If the file has to be saved or not.
File: String ? If save == true, the file name to save the mp3 to.
Speak: Boolean ? If the text has to be read out loud.
"""
import csv

with open("Datasets/transcript.csv", "r", encoding="utf8") as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        print (str(line))
        speak(str(line), "es", save=True, file=f"Tests/text-to-speech/test/audio{i}.mp3", speak=False)
# speak("", "es", save=True, slow=True, file="Tests/text-to-speech/Hola_ale.mp3", speak=False)
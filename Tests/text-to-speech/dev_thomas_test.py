if __name__ == "__main__":
    from text_to_speech import speak

    """
    Text: String ? The text to be read.
    Language: String ? The language (IETF language tag) to read the text in.
    Slow: Boolean ? Reads text more slowly.
    Save: Boolean ? If the file has to be saved or not.
    File: String ? If save == true, the file name to save the mp3 to.
    Speak: Boolean ? If the text has to be read out loud.
    """

    with open(r"datasets\transcript0_99.txt", "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            print(str(line))
            speak(str(line),
                "es",
                save=True,
                file=f"Tests/text-to-speech/tts_dev_thomas_{i}.mp3",
                speak=False)
    # speak("ejemplo", "es", save=True, slow=True, file="Tests/text-to-speech/Hola_ale.mp3", speak=False)

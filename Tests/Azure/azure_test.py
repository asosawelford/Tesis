import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(subscription="e18db7ef70cf4e04ab6d346ce693732f", region="brazilsouth")
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

# The language of the voice that speaks.
speech_config.speech_synthesis_voice_name='es-AR-ElenaNeuralsi '
# speech_config.speech_synthesis_voice_name='es-AR-TomasNeural'


speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

audio_config = speechsdk.audio.AudioOutputConfig(filename="file2.wav")
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
synthesizer.speak_text_async("Y esperaban que el jefe lo diera todo hecho.")

# # Get text from the console and synthesize to the default speaker.
# print("Enter some text that you want to speak >")
# text = input("")

# speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()



# if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
#     print("Speech synthesized for text [{}]".format(text))
# elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
#     cancellation_details = speech_synthesis_result.cancellation_details
#     print("Speech synthesis canceled: {}".format(cancellation_details.reason))
#     if cancellation_details.reason == speechsdk.CancellationReason.Error:
#         if cancellation_details.error_details:
#             print("Error details: {}".format(cancellation_details.error_details))
#             print("Did you set the speech resource key and region values?")

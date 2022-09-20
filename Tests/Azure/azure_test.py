import azure.cognitiveservices.speech as speechsdk
import os
speech_config = speechsdk.SpeechConfig(subscription="e18db7ef70cf4e04ab6d346ce693732f", region="brazilsouth")
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

# The language of the voice that speaks.
# speech_config.speech_synthesis_voice_name='es-AR-ElenaNeural'
# speech_config.speech_synthesis_voice_name='es-AR-TomasNeural'
speech_config.speech_synthesis_voice_name='es-MX-JorgeNeural'

dir_path = "datasets\\microsoft_azure\\"+speech_config.speech_synthesis_voice_name # .wav directory 
os.mkdir(dir_path)

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
with open(r"datasets\transcript0_99.txt", "r", encoding="utf-8") as a_file:
  for i, line in enumerate(a_file):
    stripped_line = line.strip()

    audio_config = speechsdk.audio.AudioOutputConfig(
        filename=f"{dir_path}/{speech_config.speech_synthesis_voice_name}{i}.wav")
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async(stripped_line)

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

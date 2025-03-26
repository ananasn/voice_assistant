from vosk_tts import Model, Synth
from playsound import playsound


class Assistant:
    def __init__(self):
        model = Model(model_name="vosk-model-tts-ru-0.7-multi")
        self.synth = Synth(model)
        self.voice = 1

    def text_to_speech(self, text="Доброе утро!"):
        self.synth.synth(text, "out.wav", speaker_id=self.voice)
        playsound('out.wav')

    def set_voice(self, voice):
        self.voice = voice


assistant = Assistant()

if __name__ == '__main__':
    assistant = Assistant()
    assistant.set_voice(4)
    assistant.text_to_speech()
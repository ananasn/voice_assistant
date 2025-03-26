import vosk
import pyaudio
import json


class Recognizer:
    def __init__(self):
        model = vosk.Model('vosk-model-small-ru-0.22')
        self.rec = vosk.KaldiRecognizer(model, 48000)
        self.init_stream()
    
    def init_stream(self):
        pa = pyaudio.PyAudio()
        self.stream = pa.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=48000,
            input=True,
            frames_per_buffer=8000
        )

    def listen(self):
        while True:
            data = self.stream.read(4000, exception_on_overflow=False)
            if len(data) and self.rec.AcceptWaveform(data):
                answer = json.loads(self.rec.Result())
                if answer['text']:
                    yield answer['text']


if __name__ == '__main__':
    rec = Recognizer()
    rec_gen = rec.listen()
    for text in rec_gen:
        print(text)
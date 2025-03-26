import time
from recognizer import Recognizer
from voice import assistant
from commands import Command


rec = Recognizer()
rec_gen = rec.listen()

assistant.text_to_speech('Привет!')
for text in rec_gen:
    rec.stream.stop_stream()
    Command(text)
    time.sleep(1)
    rec.stream.start_stream()




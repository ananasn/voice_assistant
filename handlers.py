from voice import assistant
import random


def test(text):
    assistant.text_to_speech(text)

def thanks(test):
    options = [
        'Пожалуйста',
        'Пока',
        'Не за что!'
    ]
    assistant.text_to_speech(random.choice(options))
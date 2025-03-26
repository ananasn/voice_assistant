from handlers import test, thanks
COMMANDS = [
    {'id':0, 'text': 'тест', 'handler': test},
    {'id':0, 'text': 'спасибо', 'handler': thanks},

]

class Command:
    def __init__(self, text):
        self.text = text
        self.map()

    def map(self):
        for cmd in COMMANDS:
            if cmd['text'] in self.text:
                self.run(cmd)

    def run(self, cmd):
        handler =  cmd['handler']
        handler(self.text)
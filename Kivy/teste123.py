from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import random

class Incrementador(BoxLayout):
    random_number = StringProperty()

    def __init__(self, **kwargs):
        super(Incrementador, self).__init__(**kwargs)
        self.random_number = str(random.randint(1, 100))

    def change_text(self):
        self.random_number = str(int(self.random_number) + random.randint(1, 9))

class Teste123(App):
    def build(self):
        return Incrementador()

Teste123().run()


from kivy.app import App # Importa o aplicativo
from kivy.uix.button import Button # Importa o botão

class Test(App):
    def build(self): # Método que inicializa e constroi o aplicativo
        return Button(text='Bosta!!')

Test().run()
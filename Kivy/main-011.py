from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

#Builder.load_file('toolbox.kv')
#Builder.load_file('drawingspace.kv')
#Builder.load_file('generaloptions.kv')
#Builder.load_file('statusbar.kv')

class Placar(Widget):
    pass

class Test011App(App):
    def build(self):
        return Placar()

if __name__=="__main__":
    Test011App().run()

import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout

# The Grid Layout organizes everything in a grid pattern

#class TitleBox(Widget):
#    pass

class Placar(Widget):
    pass

class GridLayoutApp(App):
    def build(self):
        return GridLayout()

if __name__=="__main__":
    GridLayoutApp().run()

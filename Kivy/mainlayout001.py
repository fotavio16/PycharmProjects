import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget


class CustomWidget(Widget):
    pass

class CustomWidgetApp(App):
    def build(self):
        return CustomWidget()

if __name__=="__main__":
    CustomWidgetApp().run()

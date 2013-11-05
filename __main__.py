from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import *


class Calculator(BoxLayout):
    wip = BooleanProperty(False)
    display = ObjectProperty(None)

    def append(self, c):
        if self.wip:
            self.display.text += c
        else:
            self.display.text = c
            self.wip = True

    def clr(self):
        self.wip = False
        self.display.text = '0'

    def ce(self):
        if self.wip:
            self.display.text = self.display.text[:-1]

    def compute(self):
        self.wip = False
        try:
            self.display.text = str(eval(self.display.text))
        except Exception:
            self.display.text = 'Error'


class Calc(App):
    def build(self):
        return Calculator()


if __name__ == "__main__":
    Calc().run()

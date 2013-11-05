from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import *


class Calculator(BoxLayout):
    wip = BooleanProperty(False)
    display = ObjectProperty(None)
    info = ObjectProperty(None)

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
            # multiply the expression with 1.0 to force a float operation
            expression = '1.0 * {0}'.format(self.display.text)
            result = eval(expression)
            self.info.text = self.display.text + '='
            self.display.text = '{0}'.format(result)
        except Exception as e:
            self.display.text = 'Error: {0}'.format(e)


class Calc(App):
    def build(self):
        return Calculator()


if __name__ == "__main__":
    Calc().run()

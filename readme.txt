calc

This is nothing but a simple calculator as a kivy training area for myself.
See http://kivy.org

TO DO:

(a) simple UI improvements: display label right-aligned, default app size

(b) multi-column and multi-row buttons +, = and 0

(c) better exception handling and error reporting in compute()

(d) Build all calculator buttons on one base class CalcButton, build all
    data entering buttons on InputButton(CalcButton).

(e) Apply colour schemes to different button types.

(f) Have InputButton automatically implement on_press, using root.append(self.text)

(g) Add status bar at the bottom, add resize grip (?)
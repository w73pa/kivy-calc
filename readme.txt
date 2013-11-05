calc

This is nothing but a simple calculator as a kivy training area for myself.
See http://kivy.org

TO DO:

(a) simple UI improvements: default app size, result label way too big, buttons too small

    done: right-aligned display
    done: added info label (shows equation which lead to current result, only after '=')

(b) multi-column and multi-row buttons +, = and 0

    how?

(c) better exception handling and error reporting in compute()

    done: slightly better (reporting exception details). Should probably temporarily switch
    to smaller font and multiline mode

(d) Build all calculator buttons on one base class CalcButton, build all
    data entering buttons on InputButton(CalcButton).

(e) Apply colour schemes to different button types.

(f) Have InputButton automatically implement on_press, using root.append(self.text)

(g) Add status bar at the bottom, add resize grip (?)

    no-op: re-size grip is there, it's just barely visible t'is all.
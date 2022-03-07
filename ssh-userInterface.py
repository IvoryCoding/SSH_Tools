#   Date:        2022/02/14
#   Author:      Emma Gillespie
#   Description: Add known ssh hosts and connect to them. Terminal command file to make ssh easier
#   Resources:   https://realpython.com/python-command-line-arguments/#:~:text=argc%20is%20an%20integer%20representing,remaining%20elements%20of%20the%20array.
#                https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/

#!/usr/bin/python3

import kivy

from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):

    def build(self):
        # return a Button() as a root widget
        return Button(text='hello world')

if __name__ == '__main__':
    TestApp().run()
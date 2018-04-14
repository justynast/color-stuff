""" simple GUI program that asks user for a color and outputs its hex code"""

from tkinter import *
from tkinter.colorchooser import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # button reffering to color picker
        Button(self,
               text = "Choose a color",
               command = self.choose_color).grid(row=0, column=0, sticky=W)

        # text output
        self.result = Text(self, width=30, height=3, wrap=WORD)
        self.result.grid(row=1, column=0, columnspan=2, sticky=W)

        # button that changes color
        self.cb = Button(self, height=1, width=20)
        self.cb.grid(row=0, column=1, sticky=W)

    def choose_color(self):
        """ asks for a color and changes color of the button"""
        self.color = askcolor()
        self.color_name = self.color[1]
        self.cb.configure(bg=self.color_name)
        self.update_txt()

    def update_txt(self):
        color_result_hex = self.color_name
        rgb_tuple = self.color[0] #gets a tuple of RGB coordinates
        color_result_rgb = ' '.join(format(x, "1.0f") for x in rgb_tuple) #transforms tuple into a string
        message = "HEX code: "
        message += color_result_hex
        message += "\nRGB code: "
        message += color_result_rgb
        self.result.delete(0.0, END)
        self.result.insert(0.0, message)



root = Tk()
root.title("Color Picker")
app = Application(root)
root.mainloop()

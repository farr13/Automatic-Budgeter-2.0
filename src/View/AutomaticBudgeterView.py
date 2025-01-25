import sys
sys.path.append('src')
import customtkinter as customtk
from Control.CategoryControl import Category_Control
from Control.History_Control import History_Control

class MainApp(customtk.CTk):
    def __init__(self):
        super().__init__()

        # MainSetup
        self.title('Automatic Budgeter')
        self.geometry('400x860')
        self.minsize(400, 860)
        self.maxsize(400,860)
        self.funds = 0

        # Main Menu
        self.cc = Category_Control(self)
        self.hh = History_Control(self)
        
        #Center Frames
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def run(self):
        self.mainloop()

app = MainApp()
if __name__ == "__main__":
    app.run()


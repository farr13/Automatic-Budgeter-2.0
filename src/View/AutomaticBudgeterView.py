import sys
sys.path.append('src')
import customtkinter as customtk
from Control.CategoryControl import Category_Control

class MainApp(customtk.CTk):
    def __init__(self):
        super().__init__()

        # MainSetup
        self.title('Automatic Budgeter')
        self.geometry('400x400')
        self.minsize(200, 200)

        # Main Menu
        self.mm = Category_Control(self)
        
        #Center Frames
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def run(self):
        self.mainloop()

app = MainApp()

if __name__ == "__main__":
    app.mainloop()


import sys
sys.path.append('src')
import customtkinter as customtk
from Control.CategoryControl import Show_Categories
from Control.CategoryControl import Create_Category

class MainApp(customtk.CTk):
    def __init__(self):
        super().__init__()

        # MainSetup
        self.title('Automatic Budgeter')
        self.geometry('400x400')
        self.minsize(200, 200)

        # Show Categories
        self.sc = Show_Categories(self)

        # Create Category Button
        self.ccb = Create_Category(self)
        
        #Center Frames
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def run(self):
        self.mainloop()

app = MainApp()

if __name__ == "__main__":
    app.mainloop()


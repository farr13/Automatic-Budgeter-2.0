import customtkinter as customtk
from Model.Entities import Category_Class
from Model.Entities import History_Class
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

        # Run Window
        self.mainloop()

    def __init__(self, parent):
        self.button = super().__init__(parent, text='Create_Category', command=Create_Category.category_creation(self))
        self.grid(row = 1, column = 0, sticky = '', pady = 20)
    
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()


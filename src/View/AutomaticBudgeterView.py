import customtkinter as customtk

class MainApp(customtk.CTk):
    def __init__(self):
        super().__init__()

        # MainSetup
        self.title('Automatic Budgeter')
        self.geometry('400x400')
        self.minsize(200, 200)

        # Create Category Button
        self.ccb = Create_Category(self)

        # Run Window
        self.mainloop()

class Create_Category(customtk.CTkButton):

    def __init__(self, parent):
        super().__init__(parent, text='Create_Category', command=self.button_callback)
        self.grid(row = 0, column = 0, padx = 20, pady = 20)
    
    def button_callback(self):
        print("This buttom is functioning")

    

app = MainApp()
app.mainloop()


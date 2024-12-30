import customtkinter as customtk

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

class Show_Categories():
    def __init__(self, parent):
        self.list = customtk.CTkScrollableFrame(parent)
        self.list.grid(pady=40,)

        for x in range(20):
            customtk.CTkButton(self.list, text='Testing').pack(padx=10)
    

class Create_Category(customtk.CTkButton):

    def button_callback(self):
        print("This buttom is functioning")

    def __init__(self, parent):
        self.button = super().__init__(parent, text='Create_Category', command=self.button_callback)
        self.grid(row = 1, column = 0, sticky = '', pady = 20)
    

app = MainApp()
app.mainloop()


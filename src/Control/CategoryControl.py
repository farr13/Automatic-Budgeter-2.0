from tkinter import messagebox
import customtkinter as customtk
import sys
sys.path.append('src')
from Model.Entities import Category_Class
from Model.Database import temp_database

class Show_Categories(customtk.CTkScrollableFrame):
    """Creates and implements the functianality of the (Show Categories) scroll tab
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(pady=40)
        customtk.CTkButton(self, text='Tester').grid(padx=10, pady=5)

    def update_display(self):
        for item in temp_database:
            print("triggered")
            customtk.CTkButton(self, text=item.name).grid(padx=10, pady=5)

class Create_Category():
    """Creates and implements the functianality of the (Create Category) button
    """

    def __init__(self, parent):
        self.button = customtk.CTkButton(parent, text='Create_Category', command=lambda : self.category_input_box())
        self.button.grid(row = 1, column = 0, sticky = '', pady = 20)

    def category_creation(self, name, amount):
        new_category = Category_Class.Category(name, amount)
        temp_database.append(new_category)
        from View.AutomaticBudgeterView import app
        app.sc.update_display()
        

    def category_input_box(self):
        """Creates and implements the functianality of the (Create Category) button
        """       
        #TO-DO 1: Create categories using the category class
        input_box1 = customtk.CTkInputDialog(text='Input a category name', title='Category Creation')
        name = input_box1.get_input()
        if name:
            input_box2 = customtk.CTkInputDialog(text='Input the money you want allocated', title='Category Creation')
            amount = input_box2.get_input()
            if amount:
                self.category_creation(name, amount)
            else:
                messagebox.showerror(title="Error", message="No text was input")
        else:
            messagebox.showerror(title="Error", message="No text was input")
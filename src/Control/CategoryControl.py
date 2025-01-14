from tkinter import messagebox
import customtkinter as customtk
from Model.Entities import Category_Class

class Create_Category(customtk.CTkButton):
    """Creates and implements the functianality of the (Create Category) button
    """
    def category_creation(self, name, amount):
        new_category = Category_Class.Category(name, amount)
        

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

class Show_Categories():
    """Creates and implements the functianality of the (Show Categories) scroll tab
    """
    def __init__(self, parent):
        self.list = customtk.CTkScrollableFrame(parent)
        self.list.grid(pady=40,)

        #TO-DO 2: Add Categories to List View
        for x in range(20):
            customtk.CTkButton(self.list, text='Testing').pack(padx=10)
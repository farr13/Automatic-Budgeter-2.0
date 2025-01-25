from tkinter import messagebox
import customtkinter as customtk
import sys
sys.path.append('src')
from Model.Entities import Category_Class
from Model.Database import temp_database

class Category_Control():
    """Creates and implements the functianality of the (Show Categories) scroll tab
    """
    def __init__(self, parent):
        # Create Category
        self.create_button = customtk.CTkButton(parent, text='Create_Category', command=lambda : self.category_input_box())
        self.create_button.pack(pady=5, padx=10, anchor="w")
        # Clear Categories
        self.clear_button = customtk.CTkButton(parent, text='Clear', command=lambda : self.clear())
        self.clear_button.pack(pady=5, padx=10, anchor="w")
        # Scrollable Frame of Categories
        self.scroll_window = customtk.CTkScrollableFrame(parent, width=350, height=250)
        self.scroll_window.pack(pady=20, padx=20, fill="both", expand=True)

    def add(self, category):
        """Adds a category to the scrollable frame"""
        #TO-DO: add functionallity for the specific categories
        category_button = customtk.CTkButton(self.scroll_window, text=category.name).pack(pady=5, padx=10, anchor="w")
        temp_database[category] = category_button
    
    def clear(self):
        """Remove all categories from the scrollable frame"""
        for widget in self.scroll_window.winfo_children():
            widget.destroy()
        temp_database.clear

    def category_creation(self, name, amount):
        """Creates a category class then calls add function"""
        new_category = Category_Class.Category(name, amount)
        self.add(new_category)

    def category_input_box(self):
        """
        Creates and implements the functianality of the (Create Category) button. 
        Creates 2 sequenced pop-up windows containing input boxes for the 
        name and money amount of the new category.
        """     
        input_box1 = customtk.CTkInputDialog(text='Input a category name', title='Category Creation')
        name = input_box1.get_input()
        if name:
            input_box2 = customtk.CTkInputDialog(text='Input the money you want allocated', title='Category Creation')
            amount = input_box2.get_input()
            if amount:
                self.category_creation(name, amount)
            else:
                messagebox.showerror(title="Error", message="No text was input")
                pass
        else:
           messagebox.showerror(title="Error", message="No text was input")
           pass
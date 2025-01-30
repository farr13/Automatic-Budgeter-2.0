from tkinter import messagebox
import customtkinter as customtk
import sys
sys.path.append('src')
from Model.Entities import Category_Class
from Model.Database import temp_database

class Category_Control():
    """Creates and implements the functianality of the Categories 
    """
    def __init__(self, parent):
        # Title
        self.title = customtk.CTkLabel(parent, text=f"Categories", font=customtk.CTkFont(size=24), fg_color="#262626", text_color="#ffffff")
        self.title.pack(side="top")
        # Colors
        # Create Category
        self.create_button = customtk.CTkButton(parent, text='Create_Category', command=lambda : self.category_input_box(), bg_color="#000000")
        self.create_button.pack(pady=5, padx=10, anchor="w")
        # Clear All Categories
        self.clear_button = customtk.CTkButton(parent, text='Clear', command=lambda : self.clear(), bg_color="#000000")
        self.clear_button.pack(pady=5, padx=10, anchor="w")
        # Remove Category
        self.remove_button = customtk.CTkButton(parent, text='Remove', command=lambda : self.remove_category(), bg_color="#000000")
        self.remove_button.pack(pady=5, padx=10, anchor="e")
        self.remove_button.place(x=250, y=35)
        # Scrollable Frame of Categories
        self.scroll_window = customtk.CTkScrollableFrame(parent, width=350, height=250, fg_color="#666699", bg_color="#000000")
        self.scroll_window.pack(pady=20, padx=20, fill="both", expand=True)
        # Shows Total Money Left
        self.funds = 0
        self.subtitle = customtk.CTkLabel(parent, text=f"Total Money left: {self.funds}", font=customtk.CTkFont(size=24), fg_color="#262626", text_color="#ffffff")
        self.subtitle.pack(pady=(0, 20), side="bottom")

    def add(self, category):
        """Adds a category to the scrollable frame"""
        category_label = customtk.CTkLabel(self.scroll_window, 
                                           text=f"Category: {category.name}\nMoney Left: ${category.money_allocated}", 
                                           text_color='white',
                                           width=300,
                                           height=100,
                                           fg_color="#01a6f8",
                                           font=('Bold', 20),
                                           corner_radius=5)
        category_label.pack(pady=5, padx=10, anchor="w")
        temp_database[category.name] = {"label" : category_label,
                                        "object" : category
        }

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
        if name not in temp_database:
            input_box2 = customtk.CTkInputDialog(text='Input the money you want allocated', title='Category Creation')
            amount = input_box2.get_input()
            if amount:
                    try:
                        self.funds += int(amount)
                        self.subtitle.configure(text=f"Total Money left: {self.funds}")
                        self.category_creation(str(name), int(amount))
                    except ValueError:
                        messagebox.showerror(title="Error", message="Must be a number!")
            else:
                messagebox.showerror(title="Error", message="No text was input")
        else:
           messagebox.showerror(title="Error", message="Text Empty or Already Exist")

    def remove_category(self):

        input_box = customtk.CTkInputDialog(text='Input a category name', title='Category Deletion')
        category_name = input_box.get_input()

        if category_name not in temp_database:
            messagebox.showerror(title="Error", message="Category Not Found")
            return
        
        for name in temp_database:
            if name == category_name:
                self.funds -= temp_database[name]["object"].money_allocated
                self.subtitle.configure(text=f"Total Money left: {self.funds}")
                temp_database[name]["label"].destroy()
                temp_database.pop(name)
                return
            
    def clear(self):
        """Remove all categories from the scrollable frame"""
        for widget in self.scroll_window.winfo_children():
            widget.destroy()
        temp_database.clear()
        self.funds = 0
        self.subtitle.configure(text=f"Total Money left: {self.funds}")
from tkinter import messagebox
import customtkinter as customtk
import sys
sys.path.append('src')
from Model.Database import temp_history
from Model.Database import temp_database

class History_Control():

    def __init__(self, parent, category_control):
        #Title
        self.title = customtk.CTkLabel(parent, text=f"Spend History", font=customtk.CTkFont(size=24), fg_color="#262626", text_color="#ffffff")
        self.title.pack(side="top") 

        # Used to acced the category functions
        self.category_controller = category_control

        # Add History
        self.addHistory_button = customtk.CTkButton(parent, text='Add Purchase', command=lambda : self.add(self.category_controller), bg_color="#000000")
        self.addHistory_button.pack(pady=5, padx=10, anchor="nw")

        #Clear History
        self.clearHistory_button = customtk.CTkButton(parent, text='Clear History', command=lambda : self.clear(), bg_color="#000000")
        self.clearHistory_button.pack(pady=10, padx=10, anchor="ne")
        self.clearHistory_button.place(x=250, y=456)

        # Scrollable Frame of History
        self.scroll_window = customtk.CTkScrollableFrame(parent, width=350, height=250, fg_color="#666699", bg_color="#000000")
        self.scroll_window.pack(pady=20, padx=20, fill="both", expand=True)
        
    
    def add(self, category_object):

        input_box = customtk.CTkInputDialog(text='Input the category the ourchase was made from', title='Item Purchased')
        category = input_box.get_input()

        if category in temp_database:

            input_box = customtk.CTkInputDialog(text='Input Name of Thing Purchased', title='Item Purchased')
            item_name = input_box.get_input()
            input_box = customtk.CTkInputDialog(text='Input Price', title='Item Purchased')
            item_price = input_box.get_input()
            input_box = customtk.CTkInputDialog(text='Type Description (Optional)', title='Item Purchased')
            item_desc = input_box.get_input()
            item_label = customtk.CTkLabel(self.scroll_window, 
                                        text=f"Name: {item_name}\nPrice: {item_price}\nDesc: {item_desc}", 
                                        font=customtk.CTkFont(size=16),
                                        fg_color="#ffffff")
            item_label.pack(side="top", pady=10)
            temp_history.append({
                "Name" : item_name,
                "Price" : item_price,
                "Desc" : item_desc,
                "Label" : item_label
            })

            temp_database[category]["object"].money_allocated -= int(item_price)
            temp_database[category]["label"].configure(text=f"Category: {category}\nMoney Left: ${temp_database[category]["object"].money_allocated}")
            category_object.funds -= int(item_price)
            category_object.subtitle.configure(text=f"Total Money left: {category_object.funds}")


        else:
            messagebox.showerror(title="Error", message="Category does not exist")

    def clear(self):
        for widget in self.scroll_window.winfo_children():
            widget.destroy()
        temp_history.clear()
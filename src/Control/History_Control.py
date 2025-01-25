from tkinter import messagebox
import customtkinter as customtk
import sys
sys.path.append('src')
from Model.Entities import History_Class
from Model.Database import temp_database

class History_Control():

    def __init__(self, parent):
        #Title
        self.title = customtk.CTkLabel(parent, text=f"Spend History", font=customtk.CTkFont(size=24))
        self.title.pack(side="top") 

        # Add History
        self.addHistory_button = customtk.CTkButton(parent, text='Add Purchase', command=lambda : self.add())
        self.addHistory_button.pack(pady=5, padx=10, anchor="nw")

        #Clear History
        self.addHistory_button = customtk.CTkButton(parent, text='Clear History', command=lambda : self.clear())
        self.addHistory_button.pack(pady=10, padx=10, anchor="ne")
        self.addHistory_button.place(x=250, y=456)
        # Scrollable Frame of History
        self.scroll_window = customtk.CTkScrollableFrame(parent, width=350, height=250)
        self.scroll_window.pack(pady=20, padx=20, fill="both", expand=True)
    
    def add(self):
        print("To Be Implemented")
    
    def clear(self):
        print("To Be Implemented")
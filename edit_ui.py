import tkinter as tk

class EditUI:
    def __init__(self, basic_ui):
        self.basic_ui = basic_ui
        self.window = basic_ui.window
        self.colours = basic_ui.colours
        self.components = basic_ui.components
        
        self.destroy()
    
    def destroy(self):
        for key, val in list(self.components.items()):
            if "canvas" in key:
                val.delete("all")
            
            try:
                val.destroy()
            except:
                pass
            
            del self.components[key]

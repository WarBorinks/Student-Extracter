import tkinter as tk

class ExtractUI:
    def __init__(self, window, colours, components):
        self.window = window
        self.colours = colours
        self.components = components
        
        self.destroy()
        self.create_components()
    
    def destroy(self):
        for key, val in list(self.components.items()):
            try:
                val.destroy()
            except:
                pass
            
            del self.components[key]
    
    def create_components(self):
        pass

if __name__ == "__main__" or __name__ != "__main__":
    pass

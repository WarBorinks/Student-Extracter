import sys
import tkinter as tk

class BasicUI:
    width, height = 800, 600
    x, y = 400, 100
    
    def __init__(self):
        self.init()
        self.window.mainloop()
        
        self.protocol()
    
    def __del__(self):
        self.x = self.window.winfo_x()
        self.y = self.window.winfo_y()
    
    def init(self):
        self.window = tk.Tk()
        self.window.title("Student Extracter")
        self.window.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self.window.resizable(False, False)
        
    def protocol(self):
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def on_closing(self):
        sys.exit()

while True:
    p = BasicUI()
    del p

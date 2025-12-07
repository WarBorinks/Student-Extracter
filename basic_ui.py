import sys
import tkinter as tk

class BasicUI:
    width, height = 800, 600
    x, y = 400, 100
    
    def __init__(self):
        self.create_root_window()
        
        self.protocol()
        
        self.window.mainloop()
    
    def create_root_window(self):
        """主窗口"""
        
        self.window = tk.Tk()
        self.window.title("Student Extracter")
        self.window.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self.window.resizable(False, False)
        self.window.iconbitmap(".\\icon.ico")
        
    def protocol(self):
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def on_closing(self):
        sys.exit()

while True:
    p = BasicUI()
    del p

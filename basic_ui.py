import sys
import tkinter as tk

class BasicUI:
    width, height = 800, 600
    x, y = 400, 100
    
    def __init__(self):
        self.create_root_window()
        self.create_basic_component()
        
        self.protocol()
        
        self.window.mainloop()
    
    def create_root_window(self):
        """主窗口"""
        
        self.window = tk.Tk()
        self.window.title("Student Extracter")
        self.window.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self.window.resizable(False, False)
        self.window.iconbitmap(".\\icon.ico")
        
        self.components = {}
    
    def create_basic_component(self):
        """创建基本组件"""
        
        # 按钮容器
        self.components["frame_edit_extract"] = tk.Frame(self.window)
        self.components["frame_edit_extract"].place(relx=0.5, rely=0.5, relwidth=0.6, relheight=0.1, anchor="center")
        
        # 按钮-编辑
        self.components["button_edit"] = tk.Button(self.components["frame_edit_extract"], text="编辑")
        self.components["button_edit"].place(relx=0.15, rely=0.5, relwidth=0.3, relheight=1, anchor="center")
        
        # 按钮-抽取
        self.components["button_extract"] = tk.Button(self.components["frame_edit_extract"], text="抽取")
        self.components["button_extract"].place(relx=0.85, rely=0.5, relwidth=0.3, relheight=1, anchor="center")
        
    def protocol(self):
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def on_closing(self):
        sys.exit()

while True:
    p = BasicUI()
    del p

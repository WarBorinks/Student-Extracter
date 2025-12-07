import tkinter as tk

class ExtractUI:
    """抽取用户界面"""
    
    width, height = 800, 600
    x, y = 400, 100
    
    colours = {
        "window_bg": "#65A8D7"
    }
    components = {}
    
    def __init__(self):
        """构造函数"""
        
        self.create_root_window()
        
        self.protocol()
        
        self.window.mainloop()
    
    def create_root_window(self):
        """创建窗口"""
        
        self.window = tk.Tk()
        self.window.title("Extract")
        self.window.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self.window.resizable(False, False)
        self.window.iconbitmap(".\\icon.ico")
        self.window.configure(bg=self.colours["window_bg"])
        
    def protocol(self):
        """绑定事件"""
        
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def on_closing(self):
        """当窗口关闭时"""
        
        self.window.destroy()

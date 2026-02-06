import sys
import tkinter as tk

from extract_ui import ExtractUI

class BasicUI:
    width, height = 800, 600
    x, y = 400, 100
    
    colours = {
        "window_bg": "#8FD8EB"
    }
    components = {}
    
    def __init__(self):
        """构造函数"""
        
        self.create_root_window()
        
        self.protocol()
        
        self.window.mainloop()
    
    def create_root_window(self):
        
        self.window = tk.Tk()
        self.window.title("Student Extracter")
        self.window.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self.window.resizable(False, False)
        self.window.iconbitmap(".\\icon.ico")
        self.window.configure(bg=self.colours["window_bg"])
        
        self.create_basic_components()
    
    def create_basic_components(self):
        self.components["label_title_studentextracter"] = tk.Label(
            self.window, text="学生抽取器", bg=self.colours["window_bg"], font=("微软雅黑", 32)
        )
        self.components["label_title_studentextracter"].place(
            relx=0.5, rely=0.1, anchor="center"
        )
        
        self.components["canvas_edit_extract_exit"] = tk.Canvas(self.window, bg=self.colours["window_bg"], highlightthickness=0)
        self.components["canvas_edit_extract_exit"].place(
            relx=0.5, rely=0.5, width=310, height=310, anchor="center"
        )
        
        self.components["arc_button_edit"] = self.components["canvas_edit_extract_exit"].create_arc(
            5, 5, 305, 305, start=90, extent=80, fill="#BAD23E", outline="#4286A3"
        )
        self.components["arc_button_edit_text"] = self.components["canvas_edit_extract_exit"].create_text(
            90, 90, text="编辑", font=("微软雅黑", 24)
        )
        
        self.components["arc_button_extract"] = self.components["canvas_edit_extract_exit"].create_arc(
            5, 5, 305, 305, start=10, extent=80, fill="#3DD747", outline="#4286A3"
        )
        self.components["arc_button_extract_text"] = self.components["canvas_edit_extract_exit"].create_text(
            220, 90, text="抽取", font=("微软雅黑", 24)
        )
        
        self.components["arc_button_exit"] = self.components["canvas_edit_extract_exit"].create_arc(
            5, 5, 305, 305, start=170, extent=200, fill="#3D95B8", outline="#4286A3"
        )
        self.components["arc_button_exit_text"] = self.components["canvas_edit_extract_exit"].create_text(
            155, 240, text="退出", font=("微软雅黑", 24)
        )
        
        self.components["oval_comingsoon"] = self.components["canvas_edit_extract_exit"].create_oval(
            110, 110, 200, 200, fill="#E8744E", outline="#4286A3"
        )
        self.components["oval_comingsoon_text"] = self.components["canvas_edit_extract_exit"].create_text(
            155, 155, text="敬请期待", font=("微软雅黑", 16)
        )
        
    def protocol(self):
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.components["canvas_edit_extract_exit"].tag_bind(
            self.components["arc_button_edit"], "<Button-1>", lambda e: self.enter_edit_ui()
        )
        self.components["canvas_edit_extract_exit"].tag_bind(
            self.components["arc_button_edit_text"], "<Button-1>", lambda e: self.enter_edit_ui()
        )
        
        self.components["canvas_edit_extract_exit"].tag_bind(
            self.components["arc_button_extract"], "<Button-1>", lambda e: self.enter_extract_ui()
        )
        self.components["canvas_edit_extract_exit"].tag_bind(
            self.components["arc_button_extract_text"], "<Button-1>", lambda e: self.enter_extract_ui()
        )
        
        self.components["canvas_edit_extract_exit"].tag_bind(
            self.components["arc_button_exit"], "<Button-1>", lambda e: self.on_closing()
        )
        self.components["canvas_edit_extract_exit"].tag_bind(
            self.components["arc_button_exit_text"], "<Button-1>", lambda e: self.on_closing()
        )
    
    def enter_edit_ui(self):
        pass
    
    def enter_extract_ui(self):
        ExtractUI(self.window, self.colours, self.components)
    
    def on_closing(self):
        self.window.destroy()
        sys.exit()

if __name__ == "__main__":
    p = BasicUI()

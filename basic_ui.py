import sys
import tkinter as tk

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
        self.window.configure(bg=self.colours["window_bg"])
    
    def create_basic_component(self):
        """创建基本组件"""
        
        # 标签-标题-学生抽取器
        self.components["label_title_studentextracter"] = tk.Label(
            self.window, text="学生抽取器", bg=self.colours["window_bg"], font=("微软雅黑", 32)
        )
        self.components["label_title_studentextracter"].place(
            relx=0.5, rely=0.1, anchor="center"
        )
        
        # 画布-编辑-抽取-退出
        self.components["canvas_edit_extract_exit"] = tk.Canvas(self.window, bg=self.colours["window_bg"], highlightthickness=0)
        self.components["canvas_edit_extract_exit"].place(
            relx=0.5, rely=0.5, width=310, height=310, anchor="center"
        )
        
        # 扇形-按钮-编辑
        self.components["arc_button_edit"] = self.components["canvas_edit_extract_exit"].create_arc(
            5, 5, 305, 305, start=90, extent=80, fill="#BAD23E", outline="#4286A3"
        )
        self.components["arc_button_edit_text"] = self.components["canvas_edit_extract_exit"].create_text(
            90, 90, text="编辑", font=("微软雅黑", 24)
        )
        
        # 扇形-按钮-抽取
        self.components["arc_button_extract"] = self.components["canvas_edit_extract_exit"].create_arc(
            5, 5, 305, 305, start=10, extent=80, fill="#3DD747", outline="#4286A3"
        )
        self.components["arc_button_extract_text"] = self.components["canvas_edit_extract_exit"].create_text(
            220, 90, text="抽取", font=("微软雅黑", 24)
        )
        
        # 扇形-按钮-退出
        self.components["arc_button_exit"] = self.components["canvas_edit_extract_exit"].create_arc(
            5, 5, 305, 305, start=170, extent=200, fill="#3D95B8", outline="#4286A3"
        )
        self.components["arc_button_exit_text"] = self.components["canvas_edit_extract_exit"].create_text(
            155, 240, text="退出", font=("微软雅黑", 24)
        )
        
        # 圆形-敬请期待
        self.components["oval_comingsoon"] = self.components["canvas_edit_extract_exit"].create_oval(
            110, 110, 200, 200, fill="#E8744E", outline="#4286A3"
        )
        self.components["oval_comingsoon_text"] = self.components["canvas_edit_extract_exit"].create_text(
            155, 155, text="敬请期待", font=("微软雅黑", 16)
        )
        
    def protocol(self):
        """绑定事件"""
        
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
        """进入编辑界面"""
        
        pass
    
    def enter_extract_ui(self):
        """进入抽取界面"""
        
        pass
    
    def on_closing(self):
        """当窗口关闭时"""
        
        sys.exit()

while True:
    p = BasicUI()
    del p

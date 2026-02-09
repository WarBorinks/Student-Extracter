import random, time
import tkinter as tk

from basic_extracter import extract_students

class ExtractUI:
    keys = [
        "nw", "w", "sw", "s", "se", "e", "ne", "n"
    ]
    
    def __init__(self, basic_ui):
        self.basic_ui = basic_ui
        self.window = basic_ui.window
        self.colours = basic_ui.colours
        self.components = basic_ui.components
        
        self.destroy()
        self.create_extract_components()
    
    def destroy(self):
        for key, val in list(self.components.items()):
            if "canvas" in key:
                val.delete("all")
            
            try:
                val.destroy()
            except:
                pass
            
            del self.components[key]
    
    def create_extract_components(self):
        self.components["label_title_extracter"] = tk.Label(
            self.window, text="抽取器", bg=self.colours["window_bg"], font=("微软雅黑", 24)
        )
        self.components["label_title_extracter"].place(
            relx=0.5, rely=0.1, anchor="center"
        )
        
        self.components["canvas_extract"] = tk.Canvas(
            self.window, bg=self.colours["window_bg"], highlightthickness=0
        )
        self.components["canvas_extract"].place(
            relx=0.5, rely=0.5, width=300, height=300, anchor="center"
        )
        
        self.components["rect_button_extract"] = self.components["canvas_extract"].create_rectangle(
            100, 100, 200, 200, fill="#3DD747", outline="#109309", width=2
        )
        self.components["rect_button_extract_text"] = self.components["canvas_extract"].create_text(
            150, 150, text="抽取", font=("微软雅黑", 24)
        )
        
        self.components["rect_label_name"] = {}
        self.components["rect_label_name"]["nw"] = self.components["canvas_extract"].create_rectangle(
            0, 0, 100, 100, fill="#4286A3", outline="#8FD8EB", width=2
        )
        self.components["rect_label_name"]["w"] = self.components["canvas_extract"].create_rectangle(
            0, 100, 100, 200, fill="#4286A3", outline="#8FD8EB", width=2
        )
        self.components["rect_label_name"]["sw"] = self.components["canvas_extract"].create_rectangle(
            0, 200, 100, 300, fill="#4286A3", outline="#8FD8EB", width=2
        )
        self.components["rect_label_name"]["s"] = self.components["canvas_extract"].create_rectangle(
            100, 200, 200, 300, fill="#4286A3", outline="#8FD8EB", width=2
        )
        self.components["rect_label_name"]["se"] = self.components["canvas_extract"].create_rectangle(
            200, 200, 300, 300, fill="#4286A3", outline="#8FD8EB", width=2
        )
        self.components["rect_label_name"]["e"] = self.components["canvas_extract"].create_rectangle(
            200, 100, 300, 200, fill="#4286A3", outline="#8FD8EB", width=2
        )
        self.components["rect_label_name"]["ne"] = self.components["canvas_extract"].create_rectangle(
            200, 0, 300, 100, fill="#4286A3", outline="#8FD8EB", width=2
        )
        self.components["rect_label_name"]["n"] = self.components["canvas_extract"].create_rectangle(
            100, 0, 200, 100, fill="#4286A3", outline="#8FD8EB", width=2
        )
        
        self.components["canvas_back"] = tk.Canvas(
            self.window, bg=self.colours["window_bg"], highlightthickness=0
        )
        self.components["canvas_back"].place(
            relx=0.0625, rely=0.9375, width=100, height=75, anchor="center"
        )
        
        self.components["rect_button_back"] = self.components["canvas_back"].create_rectangle(
            0, 0, 100, 75, fill="#E31D1D", outline="#C10D0D", width=2
        )
        self.components["rect_button_back_text"] = self.components["canvas_back"].create_text(
            50, 37.5, text="返回", font=("微软雅黑", 24)
        )
        
        self.protocol()
    
    def protocol(self):
        self.components["canvas_back"].tag_bind(
            self.components["rect_button_back"], "<Button-1>", lambda e: self.basic_ui.exit_extract_ui()
        )
        self.components["canvas_back"].tag_bind(
            self.components["rect_button_back_text"], "<Button-1>", lambda e: self.basic_ui.exit_extract_ui()
        )
        
        self.components["canvas_extract"].tag_bind(
            self.components["rect_button_extract"], "<Button-1>", lambda e: self.start_to_extract()
        )
        self.components["canvas_extract"].tag_bind(
            self.components["rect_button_extract_text"], "<Button-1>", lambda e: self.start_to_extract()
        )
    
    def start_to_extract(self):
        self.students = extract_students("default.students")
        i = 0
        
        
        self.components["rect_label_name_text"] = {}
        for key in self.components["rect_label_name"].keys():
            x1, y1, x2, y2 = self.components["canvas_extract"].coords(self.components["rect_label_name"][key])
            x, y = (x1 + x2) / 2, (y1 + y2) / 2
            self.components["rect_label_name_text"][key] = self.components["canvas_extract"].create_text(
                x, y, text=self.students[i], font=("微软雅黑", 16)
            )
            i += 1
            self.components["canvas_extract"].itemconfig(self.components["rect_label_name_text"][key], state="hidden")
        del i
    
        self.name_index, self.animation_time, self.animation_count, self.extracted_student = 0, 1.5, 0, ""
        self.extract_animation()
    
    def extract_animation(self):
        last_index = 7 if self.name_index == 0 else self.name_index - 1
        self.components["canvas_extract"].itemconfig(
            self.components["rect_label_name"][self.keys[last_index]], fill="#4286A3"
        )
        self.components["canvas_extract"].itemconfig(
            self.components["rect_label_name_text"][self.keys[last_index]], state="hidden"
        )
        
        if self.animation_time > 2:
            self.extracted_student = self.students[self.name_index]
            return
        
        key = self.keys[self.name_index]
        self.components["canvas_extract"].itemconfig(
            self.components["rect_label_name"][key], fill="#C41DD3"
        )
        self.components["canvas_extract"].itemconfig(
            self.components["rect_label_name_text"][key], state="normal"
        )
        
        self.name_index = (self.name_index + 1) % 8
        self.animation_count += 1
        self.animation_time = self.get_wait_time(self.animation_time, self.animation_count)
        
        self.window.after(int(self.animation_time * 1000), self.extract_animation)
    
    def get_wait_time(self, t, cnt):
        if cnt > 64:
            return t * random.uniform(1.1, 1.3)
        else:
            return t * random.uniform(0.1, 0.8)

if __name__ == "__main__" or __name__ != "__main__":
    pass

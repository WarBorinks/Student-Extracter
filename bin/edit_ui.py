import os
import tkinter as tk

from tkinter import filedialog
from tkinter import ttk

from helper import read, write

from choose_ui import ChooseUI

class EditUI:
    width, height = 1000, 600
    
    def __init__(self, basic_ui):
        self.basic_ui = basic_ui
        self.window = basic_ui.window
        self.settings = basic_ui.settings
        self.colours = basic_ui.colours
        self.components = basic_ui.components
        
        self.destroy()
        self.resize_window(self.width, self.height)
        
        self.create_edit_components()
    
    def destroy(self):
        for key, val in list(self.components.items()):
            if "canvas" in key:
                val.delete("all")
            
            try:
                val.destroy()
            except:
                pass
            
            del self.components[key]
        
        try:
            del self.data
        except:
            pass
    
    def resize_window(self, width, height):
        self.window.geometry(f"{width}x{height}+{self.basic_ui.x}+{self.basic_ui.y}")
    
    def create_edit_components(self):
        self.create_toolbar()
        self.create_table()
        
        self.refresh_data()
        self.refresh_table()
        self.refresh_index()
        
        self.protocol()
    
    def refresh_data(self, path=None):
        student = {}
        if path:
            student = read(path)
        else:
            student = read(self.settings["default"])
        
        self.data = []
        if student:
            for name, prob in student.items():
                self.data.append({
                    "name": name,
                    "prob": prob
                })
        
    def refresh_table(self):
        for row in self.components["tree_table"].get_children():
            self.components["tree_table"].delete(row)
        
        for item in self.data:
            self.components["tree_table"].insert(
                "", "end", values=(item["name"], f"{item['prob']*100:.1f}")
            )
        
    def refresh_index(self):
        name, new_index = self.settings["default"], ""
        if name == "./default.students":
            new_index = "#0"
        else:
            new_index = name[3:5]
        
        self.components["canvas_edit_toolbar"].itemconfig(
            self.components["rect_label_index"],
            text=new_index
        )
    
    def create_toolbar(self):
        self.components["canvas_edit_toolbar"] = tk.Canvas(
            self.window, bg="#2195C6", highlightthickness=0
        )
        self.components["canvas_edit_toolbar"].place(
            relx=0, rely=0, width=1000, height=50, anchor="nw"
        )
        
        self.components["rect_button_add"] = self.components["canvas_edit_toolbar"].create_rectangle(
            0, 0, 130, 50, fill="#1B26A4", outline="#4286A3"
        )
        self.components["rect_button_add_text"] = self.components["canvas_edit_toolbar"].create_text(
            65, 25, text="添加", font=("微软雅黑", 24), fill="#FFFFFF"
        )
        
        self.components["rect_button_delete"] = self.components["canvas_edit_toolbar"].create_rectangle(
            134, 0, 264, 50, fill="#1B26A4", outline="#4286A3"
        )
        self.components["rect_button_delete_text"] = self.components["canvas_edit_toolbar"].create_text(
            199, 25, text="删除", font=("微软雅黑", 24), fill="#FFFFFF"
        )
        
        self.components["rect_button_import"] = self.components["canvas_edit_toolbar"].create_rectangle(
            268, 0, 398, 50, fill="#1B26A4", outline="#4286A3"
        )
        self.components["rect_button_import_text"] = self.components["canvas_edit_toolbar"].create_text(
            333, 25, text="导入", font=("微软雅黑", 24), fill="#FFFFFF"
        )
        
        self.components["rect_button_export"] = self.components["canvas_edit_toolbar"].create_rectangle(
            402, 0, 532, 50, fill="#1B26A4", outline="#4286A3"
        )
        self.components["rect_button_export_text"] = self.components["canvas_edit_toolbar"].create_text(
            467, 25, text="导出", font=("微软雅黑", 24), fill="#FFFFFF"
        )
        
        self.components["rect_button_save"] = self.components["canvas_edit_toolbar"].create_rectangle(
            536, 0, 666, 50, fill="#1B26A4", outline="#4286A3"
        )
        self.components["rect_button_save_text"] = self.components["canvas_edit_toolbar"].create_text(
            602, 25, text="存档", font=("微软雅黑", 24), fill="#FFFFFF"
        )
        
        self.components["rect_button_load"] = self.components["canvas_edit_toolbar"].create_rectangle(
            670, 0, 800, 50, fill="#1B26A4", outline="#4286A3"
        )
        self.components["rect_button_load_text"] = self.components["canvas_edit_toolbar"].create_text(
            735, 25, text="读档", font=("微软雅黑", 24), fill="#FFFFFF"
        )
        
        self.components["rect_label_index"] = self.components["canvas_edit_toolbar"].create_text(
            825, 25, text="", font=("微软雅黑", 15), fill="#FFFFFF"
        )
        
        self.components["rect_button_back"] = self.components["canvas_edit_toolbar"].create_rectangle(
            850, 0, 1000, 50, fill="#1B82A4", outline="#4286A3"
        )
        self.components["rect_button_back_text"] = self.components["canvas_edit_toolbar"].create_text(
            925, 25, text="返回", font=("微软雅黑", 24)
        )
        
    def create_table(self):
        self.components["style"] = ttk.Style()
        self.components["style"].theme_use("default")
        
        self.components["style"].configure(
            "Treeview",
            background="#FFFFFF",
            font=("微软雅黑", 15),
            rowheight=50
        )
        self.components["style"].configure(
            "Treeview.Heading",
            background="#372DA8",
            font=("微软雅黑", 20, "bold"),
            relief="flat"
        )
        
        self.components["style"].configure(
            "Vertical.TScrollbar",
            relief="flat"
        )
        
        self.components["style"].map(
            "Treeview",
            background=[("selected", "#171A71")],
            foreground=[("selected", "#FFFFFF")]
        )
        self.components["style"].map(
            "Treeview.Heading",
            background=[("hover", "#372DA8")]
        )
        
        self.components["tree_table"] = ttk.Treeview(
            self.window, columns=("name", "prob"), show="headings"
        )
        self.components["tree_table"].place(
            x=0, y=50, width=1000, height=550, anchor="nw"
        )
        
        self.components["tree_table"].heading(
            "name", text="姓名"
        )
        self.components["tree_table"].column(
            "name", width=500, anchor="center"
        )
        
        self.components["tree_table"].heading(
            "prob", text="概率(%)"
        )
        self.components["tree_table"].column(
            "prob", width=500, anchor="center"
        )
        
        self.components["tree_table_scrollbar"] = ttk.Scrollbar(
            self.window, orient="vertical", command=self.components["tree_table"].yview
        )
        self.components["tree_table_scrollbar"].place(
            x=1000, y=50, width=20, height=550, anchor="ne"
        )
        
        self.components["tree_table"].configure(
            yscrollcommand=self.components["tree_table_scrollbar"].set
        )
    
    def protocol(self):
        self.components["canvas_edit_toolbar"].tag_bind(
            self.components["rect_button_add"], "<Button-1>", lambda e: self.on_add()
        )
        self.components["canvas_edit_toolbar"].tag_bind(
            self.components["rect_button_add_text"], "<Button-1>", lambda e: self.on_add()
        )
        
        self.components["canvas_edit_toolbar"].tag_bind(
            self.components["rect_button_delete"], "<Button-1>", lambda e: self.on_delete()
        )
        self.components["canvas_edit_toolbar"].tag_bind(
            self.components["rect_button_delete_text"], "<Button-1>", lambda e: self.on_delete()
        )
        
        self.components["canvas_edit_toolbar"].tag_bind(
            self.components["rect_button_import"], "<Button-1>", lambda e: self.on_import()
        )
        self.components["canvas_edit_toolbar"].tag_bind(
            self.components["rect_button_import_text"], "<Button-1>", lambda e: self.on_import()
        )
        
        self.components["canvas_edit_toolbar"].tag_bind(
            self.components["rect_button_export"], "<Button-1>", lambda e: self.on_export()
        )
        self.components["canvas_edit_toolbar"].tag_bind(
            self.components["rect_button_export_text"], "<Button-1>", lambda e: self.on_export()
        )
        
        self.components["canvas_edit_toolbar"].tag_bind(
            self.components["rect_button_save"], "<Button-1>", lambda e: self.on_save()
        )
        self.components["canvas_edit_toolbar"].tag_bind(
            self.components["rect_button_save_text"], "<Button-1>", lambda e: self.on_save()
        )
        
        self.components["canvas_edit_toolbar"].tag_bind(
            self.components["rect_button_load"], "<Button-1>", lambda e: self.on_load()
        )
        self.components["canvas_edit_toolbar"].tag_bind(
            self.components["rect_button_load_text"], "<Button-1>", lambda e: self.on_load()
        )
        
        self.components["canvas_edit_toolbar"].tag_bind(
            self.components["rect_button_back"], "<Button-1>", lambda e: self.basic_ui.exit_edit_ui()
        )
        self.components["canvas_edit_toolbar"].tag_bind(
            self.components["rect_button_back_text"], "<Button-1>", lambda e: self.basic_ui.exit_edit_ui()
        )
        
        self.components["tree_table"].bind(
            "<Double-1>", lambda e: self.on_edit(e)
        )
        
    def on_add(self):
        self.data.append({
            "name": f"学生{len(self.data) + 1}",
            "prob": 0.0
        })
        
        self.refresh_table()
        
        self.components["tree_table"].yview_moveto(1.0)
    
    def on_delete(self):
        sel = self.components["tree_table"].selection()
        if not sel:
            return
        
        for item in sel:
            idx = self.components["tree_table"].index(item)
            del self.data[idx]
        
        self.recalc_prob()
        
        self.refresh_table()
    
    def on_import(self):
        file_path = filedialog.askopenfilename(
            parent=self.window,
            title="导入",
            filetypes=[("名单文件", "*.students"), ("JSON 文件", "*.json")]
        )
        
        if file_path:
            file_name = f"./#{os.path.basename(file_path)}"
            self.settings["default"] = file_name
            self.settings["saves"].append(file_name)
            
            self.refresh_data(file_path)
            self.refresh_table()
            self.refresh_index()
            
            self.save_data()
    
    def save_data(self, name=None):
        if name:
            write(name, self.data)
        else:
            write(self.settings["default"], self.data)
            
        write("./settings.json", self.settings, False)
        
        self.basic_ui.not_save = False
    
    def on_export(self):
        file_path = filedialog.asksaveasfilename(
            parent=self.window,
            title="导出",
            initialfile="students",
            defaultextension=".students",
            filetypes=[("名单文件", "*.students"), ("JSON 文件", "*.json")]
        )
        
        write(file_path, self.data)
    
    def on_save(self):
        number = len(self.settings["saves"]) + 1
        self.settings["saves"].append(f"./#{number}.students")
        self.refresh_index()
        
        self.save_data(f"./#{number}.students")
        
        def rename(new_name):
            self.components["canvas_edit_toolbar"].itemconfig(
                self.components["rect_button_save_text"],
                text=new_name
            )
        
        rename("OK!")
        self.window.after(1000, lambda: rename("存档"))
    
    def on_load(self):
        self.save_data()
        
        self.choose_ui = ChooseUI(self)
    
    def exit_choose_ui(self):
        self.choose_ui.destroy()
        del self.choose_ui
        self.create_edit_components()
        
        self.refresh_data()
        self.refresh_table()
        self.refresh_index()
        
        self.basic_ui.not_save = True
    
    def on_edit(self, pos):
        col = self.components["tree_table"].identify_column(pos.x)
        row = self.components["tree_table"].identify_row(pos.y)
        if not row:
            return
        
        self.inline_edit(row, col)
    
    def inline_edit(self, row, col):
        pos = self.components["tree_table"].bbox(row, col)
        if not pos:
            return
        
        x, y, width, height = pos
        entry = tk.Entry(
            self.components["tree_table"], font=("微软雅黑", 15), justify="center", relief="flat"
        )
        entry.place(
            x=x, y=y, width=width, height=height
        )
        
        value = self.components["tree_table"].item(row, "values")[int(col[1:]) - 1]
        entry.insert(0, value)
        entry.select_range(0, "end")
        entry.focus_set()
        
        def on_enter():
            new_value = entry.get()
            
            item_index = self.components["tree_table"].index(row)
            if col == "#1":
                self.data[item_index]["name"] = new_value
            else:
                try:
                    new_value = float(new_value) / 100
                except:
                    pass
                
                self.recalc_prob(item_index, new_value)
            
            self.refresh_table()
            entry.destroy()
            
        def on_cancel():
            entry.destroy()
        
        entry.bind("<Return>", lambda e: on_enter())
        entry.bind("<FocusOut>", lambda e: on_enter())
        entry.bind("<Escape>", lambda e: on_cancel())
        
    def recalc_prob(self, item_index=-1, new_value=None):
        sum = 0
        for i, item in enumerate(self.data):
            if i == item_index:
                sum += new_value
            else:
                sum += item["prob"]
        
        for i, item in enumerate(self.data):
            if i == item_index:
                self.data[i]["prob"] = round(new_value / sum, 3)
            else:
                self.data[i]["prob"] = round(item["prob"] / sum, 3)

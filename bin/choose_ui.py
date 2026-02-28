from tkinter import ttk

class ChooseUI:
    def __init__(self, edit_ui):
        self.edit_ui = edit_ui
        self.window = edit_ui.window
        self.colours = edit_ui.colours
        self.components = edit_ui.components
        self.settings = edit_ui.settings
        
        self.destroy()
        self.create_choose_components()
    
    def destroy(self):
        for key, val in list(self.components.items()):
            if "canvas" in key:
                val.delete("all")
            
            try:
                val.destroy()
            except:
                pass
            
            del self.components[key]
    
    def create_choose_components(self):
        self.components["tree_choice"] = ttk.Treeview(
            self.window, columns=("choice",), show=""
        )
        self.components["tree_choice"].place(
            x=20, y=20, width=960, height=560, anchor="nw"
        )
        
        self.components["tree_choice"].column(
            "choice", width=940, anchor="center"
        )
        
        self.components["tree_choice_scrollbar"] = ttk.Scrollbar(
            self.window, orient="vertical", command=self.components["tree_choice"].yview
        )
        self.components["tree_choice_scrollbar"].place(
            x=980, y=20, width=20, height=560, anchor="ne"
        )
        
        self.components["tree_choice"].configure(
            yscrollcommand=self.components["tree_choice_scrollbar"].set
        )
        
        self.components["tree_choice"].insert(
            "", "end", values=("./default.students")
        )
        
        for choice in self.settings["saves"]:
            self.components["tree_choice"].insert(
                "", "end", values=(choice,)
            )
        
        self.protocol()
    
    def protocol(self):
        self.components["tree_choice"].bind(
            "<Button-1>", lambda e: self.on_choose(e)
        )
        
    def on_choose(self, pos):
        row = self.components["tree_choice"].identify_row(pos.y)
        if not row:
            return
        
        name = self.components["tree_choice"].item(row, "values")[0]
        self.settings["default"] = name
        
        self.edit_ui.exit_choose_ui()

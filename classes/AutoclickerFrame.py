import customtkinter as ctk

class AutoclickerFrame(ctk.CTkFrame):
    default_fg_color="transparent"
    
    def __init__(self, master, **kwargs):
        if "fg_color" not in kwargs:
            kwargs["fg_color"] = self.default_fg_color

        super().__init__(master, **kwargs)
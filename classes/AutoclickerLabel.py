import customtkinter as ctk
from constants import DEFAULT_FONT, DEFAULT_FONT_SIZE

class AutoclickerLabel(ctk.CTkLabel):
    default_font = (DEFAULT_FONT, DEFAULT_FONT_SIZE)

    # Initialize the label
    def __init__(self, master, text, **kwargs):
        if "font" not in kwargs:
            kwargs["font"] = self.default_font
    
        super().__init__(master, text=text, **kwargs)
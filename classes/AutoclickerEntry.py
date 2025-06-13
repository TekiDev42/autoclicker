import customtkinter as ctk
from constants import DEFAULT_FONT, DEFAULT_FONT_SIZE

class AutoclickerEntry(ctk.CTkEntry):
    default_width = 100
    default_font = (DEFAULT_FONT, DEFAULT_FONT_SIZE)

    def __init__(self, master, **kwargs):
        if "width" not in kwargs:
            kwargs["width"] = self.default_width

        if "font" not in kwargs:
            kwargs["font"] = self.default_font

        super().__init__(master, **kwargs)
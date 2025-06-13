import customtkinter as ctk
from constants import DEFAULT_FONT, DEFAULT_FONT_SIZE

class AutoclickerCheckBox(ctk.CTkCheckBox):
    default_font = (DEFAULT_FONT, DEFAULT_FONT_SIZE)

    def __init__(self, master, **kwargs):
        if "font" not in kwargs:
            kwargs["font"] = self.default_font

        super().__init__(master, **kwargs)
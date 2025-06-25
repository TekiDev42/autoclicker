import customtkinter as ctk
from src.constantes.ctk_config import ENTRY_CONFIG

class AutoclickerEntry(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        if "width" not in kwargs:
            kwargs["width"] = ENTRY_CONFIG["width"]

        if "font" not in kwargs:
            kwargs["font"] = ENTRY_CONFIG["font"]

        super().__init__(master, **kwargs)
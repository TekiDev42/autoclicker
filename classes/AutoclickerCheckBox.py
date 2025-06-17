import customtkinter as ctk
from constantes.ctk_config import CHECKBOX_CONFIG

class AutoclickerCheckBox(ctk.CTkCheckBox):

    def __init__(self, master, **kwargs):
        if "font" not in kwargs:
            kwargs["font"] = CHECKBOX_CONFIG["font"]

        super().__init__(master, **kwargs)
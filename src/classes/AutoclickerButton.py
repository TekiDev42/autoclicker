import customtkinter as ctk
from src.constantes.ctk_config import BUTTON_CONFIG

class AutoclickerButton(ctk.CTkButton):

    def __init__(self, master, **kwargs):
        if "fg_color" not in kwargs:
            kwargs["fg_color"] = BUTTON_CONFIG["fg_color"]

        super().__init__(master, **kwargs)
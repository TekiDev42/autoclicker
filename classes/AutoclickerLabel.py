import customtkinter as ctk
from constantes.ctk_config import LABEL_CONFIG

class AutoclickerLabel(ctk.CTkLabel):

    # Initialize the label
    def __init__(self, master, text, **kwargs):
        if "font" not in kwargs:
            kwargs["font"] = LABEL_CONFIG["font"]
    
        super().__init__(master, text=text, **kwargs)
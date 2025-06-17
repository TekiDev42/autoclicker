import customtkinter as ctk
from constantes.ctk_config import FRAME_CONFIG

# Custom class that inherits from CTkFrame to create frames in the interface
class AutoclickerFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        # If no background color is specified, use the default color
        if "fg_color" not in kwargs:
            kwargs["fg_color"] = FRAME_CONFIG["fg_color"]

        # Call the parent constructor with parameters
        super().__init__(master, **kwargs)
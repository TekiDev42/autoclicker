import customtkinter as ctk

# Custom class that inherits from CTkFrame to create frames in the interface
class AutoclickerFrame(ctk.CTkFrame):
    # Default transparent background color
    default_fg_color="transparent"
    
    def __init__(self, master, **kwargs):
        # If no background color is specified, use the default color
        if "fg_color" not in kwargs:
            kwargs["fg_color"] = self.default_fg_color

        # Call the parent constructor with parameters
        super().__init__(master, **kwargs)
import customtkinter as ctk
import keyboard
from constants import (
    WINDOW_TITLE, WINDOW_SIZE, THEME_MODE, THEME_COLOR,
    CHANGE_KEY_BUTTON, QUIT_BUTTON, KEY_MAPPING
)
from autoclicker_core import Autoclicker

class AutoclickerGUI(ctk.CTk):
    """
    Main GUI class for the autoclicker application.
    Inherits from customtkinter's CTk for modern UI elements.
    """
    def __init__(self):
        super().__init__()
        
        # Initialize autoclicker instance and key change state
        self.autoclicker = Autoclicker()
        self.waiting_for_key = False
        
        # Window configuration
        self.title(WINDOW_TITLE)
        self.geometry(WINDOW_SIZE)
        
        # Theme configuration
        ctk.set_appearance_mode(THEME_MODE)
        ctk.set_default_color_theme(THEME_COLOR)
        
        # Create UI elements
        self.create_widgets()
        
        # Set up keyboard shortcuts
        self.update_key_bindings()
        
    def create_widgets(self):
        """
        Creates and arranges all UI elements including:
        - Title
        - Instructions
        - Delay settings
        - Click counter
        - Control buttons
        """
        # Title label
        self.title_label = ctk.CTkLabel(
            self, 
            text=WINDOW_TITLE, 
            font=("Helvetica", 24, "bold")
        )
        self.title_label.pack(pady=20)
        
        # Instructions frame with key information
        self.instructions_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.instructions_frame.pack(pady=10)
        
        self.instructions_text1 = ctk.CTkLabel(
            self.instructions_frame,
            text="Hold the key ",
            font=("Helvetica", 12)
        )
        self.instructions_text1.pack(side="left")
        
        self.instructions_key = ctk.CTkLabel(
            self.instructions_frame,
            text=self.autoclicker.control_key.upper(),
            font=("Helvetica", 12, "bold")
        )
        self.instructions_key.pack(side="left")
        
        self.instructions_text2 = ctk.CTkLabel(
            self.instructions_frame,
            text=" to activate the auto-clicker",
            font=("Helvetica", 12)
        )
        self.instructions_text2.pack(side="left")

        # Frame for delay settings
        self.delay_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.delay_frame.pack(pady=10)

        # Label for minimum delay
        self.delay_min_label = ctk.CTkLabel(
            self.delay_frame,
            text="Min delay (ms):",
            font=("Helvetica", 12)
        )
        self.delay_min_label.pack(side="left", padx=5)

        # Input field for minimum delay
        self.delay_min_entry = ctk.CTkEntry(
            self.delay_frame,
            width=100,
            font=("Helvetica", 12)
        )
        self.delay_min_entry.insert(0, str(int(self.autoclicker.delay_min * 1000)))
        self.delay_min_entry.pack(side="left", padx=5)
        self.delay_min_entry.bind("<Return>", self.update_delay)

        # Label for maximum delay
        self.delay_max_label = ctk.CTkLabel(
            self.delay_frame,
            text="Max delay (ms):",
            font=("Helvetica", 12)
        )
        self.delay_max_label.pack(side="left", padx=5)

        # Input field for maximum delay
        self.delay_max_entry = ctk.CTkEntry(
            self.delay_frame,
            width=100,
            font=("Helvetica", 12)
        )
        self.delay_max_entry.insert(0, str(int(self.autoclicker.delay_max * 1000)))
        self.delay_max_entry.pack(side="left", padx=5)
        self.delay_max_entry.bind("<Return>", self.update_delay)

        # Random delay checkbox
        self.random_delay_var = ctk.BooleanVar(value=self.autoclicker.random_delay)
        self.random_delay_checkbox = ctk.CTkCheckBox(
            self.delay_frame,
            text="Random delay",
            variable=self.random_delay_var,
            command=self.toggle_random_delay,
            font=("Helvetica", 12)
        )
        self.random_delay_checkbox.pack(side="left", padx=5)
        
        # Click counter
        self.click_counter = ctk.CTkLabel(
            self,
            text="Clicks: 0",
            font=("Helvetica", 14)
        )
        self.click_counter.pack(pady=10)

        # Button to change the key
        self.change_key_button = ctk.CTkButton(
            self,
            command=self.start_key_change,
            **CHANGE_KEY_BUTTON
        )
        self.change_key_button.pack(pady=10)
        
        # Close button
        self.quit_button = ctk.CTkButton(
            self,
            command=self.quit,
            **QUIT_BUTTON
        )
        self.quit_button.pack(pady=20)

    def convert_key(self, tk_key):
        """
        Converts Tkinter key format to keyboard library format
        Args:
            tk_key: Key in Tkinter format
        Returns:
            str: Key in keyboard library format
        """
        key = tk_key.lower()
        return KEY_MAPPING.get(key, key)

    def start_key_change(self):
        """
        Initiates the process of changing the control key
        Updates UI to indicate waiting for new key input
        """
        if not self.waiting_for_key:
            self.waiting_for_key = True
            self.change_key_button.configure(text="Press a key...")
            self.bind_all("<Key>", self.on_key_press)

    def on_key_press(self, event):
        """
        Handles key press events during key change process
        Args:
            event: Key press event from Tkinter
        """
        if self.waiting_for_key:
            new_key = self.convert_key(event.keysym)
            self.autoclicker.set_control_key(new_key)
            self.instructions_key.configure(text=new_key.upper())
            self.change_key_button.configure(text=CHANGE_KEY_BUTTON["text"])
            self.waiting_for_key = False
            self.unbind_all("<Key>")
            self.update_key_bindings()

    def update_key_bindings(self):
        """
        Updates keyboard bindings for autoclicker control
        Removes old bindings and sets up new ones for:
        - Control key press (start clicking)
        - Control key release (stop clicking)
        - F7 key (quit application)
        """
        keyboard.unhook_all()
        keyboard.on_press_key(self.autoclicker.control_key, lambda _: self.start_clicking())
        keyboard.on_release_key(self.autoclicker.control_key, lambda _: self.stop_clicking())
        keyboard.on_press_key('f7', lambda _: self.quit())
        
    def start_clicking(self):
        """
        Starts the autoclicker and updates click counter
        """
        self.autoclicker.start()
        self.click_counter.configure(text=f"Clicks: {self.autoclicker.click_count}")
        
    def stop_clicking(self):
        """
        Stops the autoclicker and updates click counter
        """
        self.autoclicker.stop()
        self.click_counter.configure(text=f"Clicks: {self.autoclicker.click_count}")

    def update_delay(self, event=None):
        """
        Updates click delay settings
        Validates input and ensures minimum delay of 10ms
        Args:
            event: Optional event parameter for binding
        """
        try:
            min_delay = int(self.delay_min_entry.get()) / 1000  # Convert to seconds
            max_delay = int(self.delay_max_entry.get()) / 1000  # Convert to seconds
            
            # Enforce minimum delay of 10ms
            if min_delay < 0.01:
                min_delay = 0.01
                self.delay_min_entry.delete(0, "end")
                self.delay_min_entry.insert(0, "10")
            
            if min_delay > 0 and max_delay >= min_delay:
                self.autoclicker.set_delay(min_delay, max_delay)
            else:
                # Restore previous values on error
                self.delay_min_entry.delete(0, "end")
                self.delay_min_entry.insert(0, str(int(self.autoclicker.delay_min * 1000)))
                self.delay_max_entry.delete(0, "end")
                self.delay_max_entry.insert(0, str(int(self.autoclicker.delay_max * 1000)))
        except ValueError:
            # Restore previous values on error
            self.delay_min_entry.delete(0, "end")
            self.delay_min_entry.insert(0, str(int(self.autoclicker.delay_min * 1000)))
            self.delay_max_entry.delete(0, "end")
            self.delay_max_entry.insert(0, str(int(self.autoclicker.delay_max * 1000)))

    def toggle_random_delay(self):
        """
        Toggles random delay mode
        When disabled, sets maximum delay equal to minimum delay
        """
        self.autoclicker.set_random_delay(self.random_delay_var.get())
        if not self.random_delay_var.get():
            self.delay_max_entry.delete(0, "end")
            self.delay_max_entry.insert(0, str(int(self.autoclicker.delay_min * 1000))) 
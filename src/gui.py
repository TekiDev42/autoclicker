import customtkinter as ctk
import keyboard
from src.constantes.ctk_config import (
    WINDOW_TITLE, WINDOW_SIZE, THEME_MODE, THEME_COLOR,
    CHANGE_KEY_BUTTON, PAUSE_BUTTON, QUIT_BUTTON, DEFAULT_FONT, DEFAULT_FONT_SIZE
)
from src.constantes.constants import KEY_MAPPING
from src.autoclicker_core import Autoclicker
from src.classes.AutoclickerLabel import AutoclickerLabel
from src.classes.AutoclickerFrame import AutoclickerFrame
from src.classes.AutoclickerButton import AutoclickerButton
from src.classes.AutoclickerEntry import AutoclickerEntry
from src.classes.AutoclickerCheckBox import AutoclickerCheckBox


class AutoclickerGUI(ctk.CTk):
    main_frame: AutoclickerFrame
    buttons_frame: AutoclickerFrame
    title_label: AutoclickerLabel
    instructions_frame: AutoclickerFrame
    delay_frame: AutoclickerFrame
    click_counter: AutoclickerLabel
    change_key_button: AutoclickerButton
    pause_button: AutoclickerButton
    quit_button: AutoclickerButton
    random_delay_var: ctk.BooleanVar
    random_delay_checkbox: AutoclickerCheckBox
    delay_min_label: AutoclickerLabel
    delay_min_entry: AutoclickerEntry
    delay_max_label: AutoclickerLabel
    delay_max_entry: AutoclickerEntry
    instructions_text1: AutoclickerLabel
    instructions_key: AutoclickerLabel
    instructions_text2: AutoclickerLabel
    waiting_for_key: bool = False
    is_paused: bool = False
    autoclicker: Autoclicker

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

    def create_widgets(self):
        """
        Creates and arranges all UI elements including:
        - Title
        - Instructions
        - Delay settings
        - Click counter
        - Control buttons
        """
        # Main container frame
        self.main_frame = AutoclickerFrame(self)
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Title label
        self.title_label = AutoclickerLabel(self.main_frame, text=WINDOW_TITLE, font=(DEFAULT_FONT, 24, "bold"))
        self.title_label.pack(pady=20)
        
        # Instructions frame with key information
        self.make_instructions_frame()

        # Instructions labels
        self.make_instructions_labels()

        # Frame for delay settings
        self.make_delay_frame()

        # Delay settings
        self.make_delay_settings()
        
        # Click counter
        self.make_click_counter()

        # buttons frame
        self.make_buttons_frame()

        # Button to change the key
        self.make_change_key_button()
        
        # Button to pause/resume
        self.make_pause_button()
        
        # Close button
        self.make_quit_button()

    def make_buttons_frame(self):
        self.buttons_frame = AutoclickerFrame(self.main_frame)
        self.buttons_frame.pack(pady=10)

    def make_change_key_button(self):
        self.change_key_button = AutoclickerButton(
            self.buttons_frame,
            command=self.start_key_change,
            **CHANGE_KEY_BUTTON
        )
        self.change_key_button.pack(side="left", padx=10)

    def make_click_counter(self):
        self.click_counter = AutoclickerLabel(self.main_frame, text="Clicks: 0")
        self.click_counter.pack(pady=10)

    def make_delay_frame(self):
        self.delay_frame = AutoclickerFrame(self.main_frame)
        self.delay_frame.pack(pady=10)

    def make_delay_settings(self):
        # Label for minimum delay
        self.delay_min_label = AutoclickerLabel(self.delay_frame, text="Min delay (ms):")
        self.delay_min_label.pack(side="left", padx=5)

        # Input field for minimum delay
        self.delay_min_entry = AutoclickerEntry(self.delay_frame)
        self.delay_min_entry.insert(0, str(int(self.autoclicker.delay_min * 1000)))
        self.delay_min_entry.pack(side="left", padx=5)
        self.delay_min_entry.bind("<Return>", self.update_delay)

        # Label for maximum delay
        self.delay_max_label = AutoclickerLabel(self.delay_frame,text="Max delay (ms):")
        self.delay_max_label.pack(side="left", padx=5)

        # Input field for maximum delay
        self.delay_max_entry = AutoclickerEntry(self.delay_frame)
        self.delay_max_entry.insert(0, str(int(self.autoclicker.delay_max * 1000)))
        self.delay_max_entry.pack(side="left", padx=5)
        self.delay_max_entry.bind("<Return>", self.update_delay)

        # Random delay checkbox
        self.random_delay_var = ctk.BooleanVar(value=self.autoclicker.random_delay)
        self.random_delay_checkbox = AutoclickerCheckBox(
            self.delay_frame,
            text="Random delay",
            variable=self.random_delay_var,
            command=self.toggle_random_delay,
        )
        self.random_delay_checkbox.pack(side="left", padx=5)

    def make_instructions_frame(self):
        self.instructions_frame = AutoclickerFrame(self.main_frame)
        self.instructions_frame.pack(pady=10)

    def make_instructions_labels(self):
        self.instructions_text1 = AutoclickerLabel(
            self.instructions_frame, 
            text="Hold the key "
        )
        
        self.instructions_key = AutoclickerLabel(
            self.instructions_frame, 
            text=self.autoclicker.control_key.upper(), 
            font=(DEFAULT_FONT, DEFAULT_FONT_SIZE, "bold")
        )
        
        self.instructions_text2 = AutoclickerLabel(
            self.instructions_frame, 
            text=" to activate the auto-clicker"
        )

        self.instructions_text1.pack(side="left")
        self.instructions_key.pack(side="left")
        self.instructions_text2.pack(side="left")

    def make_pause_button(self):
        self.pause_button = AutoclickerButton(
            self.buttons_frame,
            command=self.toggle_pause,
            **PAUSE_BUTTON
        )
        self.pause_button.pack(side="left", padx=10)

    def make_quit_button(self):
        self.quit_button = AutoclickerButton(
            self.buttons_frame,
            command=self.quit,
            **QUIT_BUTTON
        )
        self.quit_button.pack(side="left", padx=10)

    def on_key_press(self, event):
        """
        Handles key press events during key change process
        Args:
            event: Key press event from Tkinter
        """
        if self.waiting_for_key:
            new_key = self.convert_key(event.keysym)
            if new_key == None:
                return
    
            self.autoclicker.set_control_key(new_key)
            self.instructions_key.configure(text=new_key.upper())
            self.change_key_button.configure(text=CHANGE_KEY_BUTTON["text"])
            self.waiting_for_key = False
            self.unbind_all("<Key>")
            self.update_key_bindings()

    def start_clicking(self):
        """
        Starts the autoclicker and updates click counter
        """
        if not self.is_paused:
            self.autoclicker.start()
            self.click_counter.configure(text=f"Clicks: {self.autoclicker.click_count}")
        
    def start_key_change(self):
        """
        Initiates the process of changing the control key
        Updates UI to indicate waiting for new key input
        """
        if not self.waiting_for_key and not self.is_paused:
            self.waiting_for_key = True
            self.change_key_button.configure(text="Press a key...")
            self.bind_all("<Key>", self.on_key_press)

    def stop_clicking(self):
        """
        Stops the autoclicker and updates click counter
        """
        if not self.is_paused:
            self.autoclicker.stop()
            self.click_counter.configure(text=f"Clicks: {self.autoclicker.click_count}")

    def toggle_random_delay(self):
        """
        Toggles random delay mode
        When disabled, sets maximum delay equal to minimum delay
        """
        self.autoclicker.set_random_delay(self.random_delay_var.get())
        if not self.random_delay_var.get():
            self.delay_max_entry.delete(0, "end")
            self.delay_max_entry.insert(0, str(int(self.autoclicker.delay_min * 1000))) 

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

    def update_key_bindings(self):
        """
        Updates keyboard bindings for autoclicker control
        Removes old bindings and sets up new ones for:
        - Control key press (start clicking)
        - Control key release (stop clicking)
        - F7 key (quit application)
        - F8 key (pause/resume)
        """
        keyboard.unhook_all()
        keyboard.on_press_key(self.autoclicker.control_key, lambda _: self.start_clicking())
        keyboard.on_release_key(self.autoclicker.control_key, lambda _: self.stop_clicking())
        keyboard.on_press_key('f7', lambda _: self.quit())
        keyboard.on_press_key('f8', lambda _: self.toggle_pause())

    def toggle_pause(self):
        """
        Toggles the pause state of the autoclicker
        """
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.pause_button.configure(text="Resume (F8)")
            keyboard.unhook_all()
            keyboard.on_press_key('f8', lambda _: self.toggle_pause())
            keyboard.on_press_key('f7', lambda _: self.quit())
        else:
            self.pause_button.configure(text="Pause (F8)")
            self.update_key_bindings()
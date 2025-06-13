# Configuration PyAutoGUI
PYAUTOGUI_FAILSAFE = True
PYAUTOGUI_PAUSE = 0.010

# Dictionary of Tkinter key conversion to keyboard library
KEY_MAPPING = {
    'control_l': 'ctrl',
    'control_r': 'ctrl',
    'shift_l': 'shift',
    'shift_r': 'shift',
    'alt_l': 'alt',
    'alt_r': 'alt',
    'super_l': 'win',
    'super_r': 'win',
    'caps_lock': 'caps lock',
    'return': 'enter',
    'backspace': 'backspace',
    'delete': 'delete',
    'space': 'space',
    'tab': 'tab',
    'escape': 'esc',
    'up': 'up',
    'down': 'down',
    'left': 'left',
    'right': 'right',
    'home': 'home',
    'end': 'end',
    'page_up': 'page up',
    'page_down': 'page down',
    'insert': 'insert',
    'print_screen': 'print screen',
    'scroll_lock': 'scroll lock',
    'pause': 'pause',
    'num_lock': 'num lock',
    'f1': 'f1',
    'f2': 'f2',
    'f3': 'f3',
    'f4': 'f4',
    'f5': 'f5',
    'f6': 'f6',
    'f7': 'f7',
    'f8': 'f8',
    'f9': 'f9',
    'f10': 'f10',
    'f11': 'f11',
    'f12': 'f12'
}

# Interface configuration
WINDOW_TITLE = "AutoClicker"
WINDOW_SIZE = "800x400"
THEME_MODE = "dark"
THEME_COLOR = "blue"
DEFAULT_FONT = "Helvetica"
DEFAULT_FONT_SIZE = 16

# Button configuration
CHANGE_KEY_BUTTON = {
    "text": "Change the control key",
    "fg_color": "#D21175",
    "hover_color": "#A50D5C",
    "text_color": "white",
    "corner_radius": 50,
    "font": (DEFAULT_FONT, DEFAULT_FONT_SIZE)
}

# Quit button configuration
QUIT_BUTTON = {
    "text": "Quit (F7)",
    "fg_color": "red",
    "hover_color": "darkred",
    "corner_radius": 50,
    "font": (DEFAULT_FONT, DEFAULT_FONT_SIZE)
} 
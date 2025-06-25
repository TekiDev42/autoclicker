# Required libraries
import pyautogui  # For mouse and keyboard control
import time       # For managing delays
from threading import Thread  # For background click execution
import random     # For generating random delays
from src.constantes.constants import PYAUTOGUI_FAILSAFE, PYAUTOGUI_PAUSE

class Autoclicker:
    """
    Main class to manage the autoclicker.
    Allows automatic click simulation with configurable delays.
    """
    def __init__(self):
        # Control variables initialization
        self.running = False        # Autoclicker running state
        self.click_thread = None    # Thread for click execution
        self.delay_min = 0.050      # Minimum delay between clicks (in seconds)
        self.delay_max = 0.100      # Maximum delay between clicks (in seconds)
        self.click_count = 0        # Click counter
        self.control_key = 'w'   # Control key to stop/start
        self.random_delay = True    # Random delay activation
        
        # PyAutoGUI safety parameters configuration
        pyautogui.FAILSAFE = PYAUTOGUI_FAILSAFE  # Enable/disable safety feature
        pyautogui.PAUSE = PYAUTOGUI_PAUSE        # Delay between PyAutoGUI actions

    def clicker(self):
        """
        Main method that performs automatic clicks.
        Runs in a separate thread to avoid blocking the interface.
        """
        while self.running:
            pyautogui.click()  # Performs a click
            self.click_count += 1
            # Applies random or fixed delay between clicks
            if self.random_delay:
                time.sleep(random.uniform(self.delay_min, self.delay_max))
            else:
                time.sleep(self.delay_min)
        print(f"Click {self.click_count}")
        self.click_count = 0

    def start(self):
        """
        Starts the autoclicker by creating a new thread.
        """
        if not self.running:
            self.running = True
            self.click_thread = Thread(target=self.clicker)
            self.click_thread.start()
            print("Autoclicker started")

    def stop(self):
        """
        Stops the autoclicker by terminating the click thread.
        """
        if self.running:
            self.running = False
            print("Autoclicker stopped")

    def set_control_key(self, new_key):
        """
        Changes the control key used to stop/start the autoclicker.
        """
        self.control_key = new_key

    def set_delay(self, min_delay, max_delay=None):
        """
        Configures delays between clicks.
        If max_delay is not specified, uses a fixed delay.
        """
        self.delay_min = min_delay
        if max_delay is None:
            self.delay_max = min_delay
            self.random_delay = False
        else:
            self.delay_max = max_delay
            self.random_delay = True

    def set_random_delay(self, enabled):
        """
        Enables or disables random delays between clicks.
        """
        self.random_delay = enabled
        if not enabled:
            self.delay_max = self.delay_min 
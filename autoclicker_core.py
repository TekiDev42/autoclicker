import pyautogui
import time
from threading import Thread
import random
from constants import PYAUTOGUI_FAILSAFE, PYAUTOGUI_PAUSE

class Autoclicker:
    def __init__(self):
        self.running = False
        self.click_thread = None
        self.delay_min = 0.010
        self.delay_max = 0.020
        self.click_count = 0
        self.control_key = 'ctrl'
        self.random_delay = True
        
        # Configuration de PyAutoGUI
        pyautogui.FAILSAFE = PYAUTOGUI_FAILSAFE
        pyautogui.PAUSE = PYAUTOGUI_PAUSE

    def clicker(self):
        while self.running:
            pyautogui.click()
            self.click_count += 1
            if self.random_delay:
                time.sleep(random.uniform(self.delay_min, self.delay_max))
            else:
                time.sleep(self.delay_min)
        print(f"Clic {self.click_count}")
        self.click_count = 0

    def start(self):
        if not self.running:
            self.running = True
            self.click_thread = Thread(target=self.clicker)
            self.click_thread.start()
            print("Autoclicker démarré")

    def stop(self):
        if self.running:
            self.running = False
            print("Autoclicker arrêté")

    def set_control_key(self, new_key):
        self.control_key = new_key

    def set_delay(self, min_delay, max_delay=None):
        self.delay_min = min_delay
        if max_delay is None:
            self.delay_max = min_delay
            self.random_delay = False
        else:
            self.delay_max = max_delay
            self.random_delay = True

    def set_random_delay(self, enabled):
        self.random_delay = enabled
        if not enabled:
            self.delay_max = self.delay_min 
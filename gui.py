import customtkinter as ctk
import keyboard
from constants import (
    WINDOW_TITLE, WINDOW_SIZE, THEME_MODE, THEME_COLOR,
    CHANGE_KEY_BUTTON, QUIT_BUTTON, KEY_MAPPING
)
from autoclicker_core import Autoclicker

class AutoclickerGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.autoclicker = Autoclicker()
        self.waiting_for_key = False
        
        # Configuration de la fenêtre
        self.title(WINDOW_TITLE)
        self.geometry(WINDOW_SIZE)
        
        # Configuration du thème
        ctk.set_appearance_mode(THEME_MODE)
        ctk.set_default_color_theme(THEME_COLOR)
        
        # Création des widgets
        self.create_widgets()
        
        # Configuration des raccourcis clavier
        self.update_key_bindings()
        
    def create_widgets(self):
        # Titre
        self.title_label = ctk.CTkLabel(
            self, 
            text=WINDOW_TITLE, 
            font=("Helvetica", 24, "bold")
        )
        self.title_label.pack(pady=20)
        
        # Instructions
        self.instructions_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.instructions_frame.pack(pady=10)
        
        self.instructions_text1 = ctk.CTkLabel(
            self.instructions_frame,
            text="Maintenez la touche ",
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
            text=" pour activer l'auto-clicker",
            font=("Helvetica", 12)
        )
        self.instructions_text2.pack(side="left")

        # Frame pour les paramètres de délai
        self.delay_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.delay_frame.pack(pady=10)

        # Label pour le délai minimum
        self.delay_min_label = ctk.CTkLabel(
            self.delay_frame,
            text="Délai min (ms):",
            font=("Helvetica", 12)
        )
        self.delay_min_label.pack(side="left", padx=5)

        # Champ de saisie pour le délai minimum
        self.delay_min_entry = ctk.CTkEntry(
            self.delay_frame,
            width=100,
            font=("Helvetica", 12)
        )
        self.delay_min_entry.insert(0, str(int(self.autoclicker.delay_min * 1000)))
        self.delay_min_entry.pack(side="left", padx=5)
        self.delay_min_entry.bind("<Return>", self.update_delay)

        # Label pour le délai maximum
        self.delay_max_label = ctk.CTkLabel(
            self.delay_frame,
            text="Délai max (ms):",
            font=("Helvetica", 12)
        )
        self.delay_max_label.pack(side="left", padx=5)

        # Champ de saisie pour le délai maximum
        self.delay_max_entry = ctk.CTkEntry(
            self.delay_frame,
            width=100,
            font=("Helvetica", 12)
        )
        self.delay_max_entry.insert(0, str(int(self.autoclicker.delay_max * 1000)))
        self.delay_max_entry.pack(side="left", padx=5)
        self.delay_max_entry.bind("<Return>", self.update_delay)

        # Case à cocher pour le délai aléatoire
        self.random_delay_var = ctk.BooleanVar(value=self.autoclicker.random_delay)
        self.random_delay_checkbox = ctk.CTkCheckBox(
            self.delay_frame,
            text="Délai aléatoire",
            variable=self.random_delay_var,
            command=self.toggle_random_delay,
            font=("Helvetica", 12)
        )
        self.random_delay_checkbox.pack(side="left", padx=5)
        
        # Compteur de clics
        self.click_counter = ctk.CTkLabel(
            self,
            text="Clics: 0",
            font=("Helvetica", 14)
        )
        self.click_counter.pack(pady=10)

        # Bouton pour changer la touche
        self.change_key_button = ctk.CTkButton(
            self,
            command=self.start_key_change,
            **CHANGE_KEY_BUTTON
        )
        self.change_key_button.pack(pady=10)
        
        # Bouton de fermeture
        self.quit_button = ctk.CTkButton(
            self,
            command=self.quit,
            **QUIT_BUTTON
        )
        self.quit_button.pack(pady=20)

    def convert_key(self, tk_key):
        # Convertir la touche Tkinter en format keyboard
        key = tk_key.lower()
        return KEY_MAPPING.get(key, key)

    def start_key_change(self):
        if not self.waiting_for_key:
            self.waiting_for_key = True
            self.change_key_button.configure(text="Appuyez sur une touche...")
            self.bind_all("<Key>", self.on_key_press)

    def on_key_press(self, event):
        if self.waiting_for_key:
            new_key = self.convert_key(event.keysym)
            self.autoclicker.set_control_key(new_key)
            self.instructions_key.configure(text=new_key.upper())
            self.change_key_button.configure(text=CHANGE_KEY_BUTTON["text"])
            self.waiting_for_key = False
            self.unbind_all("<Key>")
            self.update_key_bindings()

    def update_key_bindings(self):
        # Supprimer les anciens bindings
        keyboard.unhook_all()
        # Ajouter les nouveaux bindings
        keyboard.on_press_key(self.autoclicker.control_key, lambda _: self.start_clicking())
        keyboard.on_release_key(self.autoclicker.control_key, lambda _: self.stop_clicking())
        keyboard.on_press_key('f7', lambda _: self.quit())
        
    def start_clicking(self):
        self.autoclicker.start()
        self.click_counter.configure(text=f"Clics: {self.autoclicker.click_count}")
        
    def stop_clicking(self):
        self.autoclicker.stop()
        self.click_counter.configure(text=f"Clics: {self.autoclicker.click_count}")

    def update_delay(self, event=None):
        try:
            min_delay = int(self.delay_min_entry.get()) / 1000  # Conversion en secondes
            max_delay = int(self.delay_max_entry.get()) / 1000  # Conversion en secondes
            
            # Vérification du délai minimum de 10ms
            if min_delay < 0.01:  # 10ms = 0.01s
                min_delay = 0.01
                self.delay_min_entry.delete(0, "end")
                self.delay_min_entry.insert(0, "10")
            
            if min_delay > 0 and max_delay >= min_delay:
                self.autoclicker.set_delay(min_delay, max_delay)
            else:
                # Restaurer les valeurs précédentes en cas d'erreur
                self.delay_min_entry.delete(0, "end")
                self.delay_min_entry.insert(0, str(int(self.autoclicker.delay_min * 1000)))
                self.delay_max_entry.delete(0, "end")
                self.delay_max_entry.insert(0, str(int(self.autoclicker.delay_max * 1000)))
        except ValueError:
            # Restaurer les valeurs précédentes en cas d'erreur
            self.delay_min_entry.delete(0, "end")
            self.delay_min_entry.insert(0, str(int(self.autoclicker.delay_min * 1000)))
            self.delay_max_entry.delete(0, "end")
            self.delay_max_entry.insert(0, str(int(self.autoclicker.delay_max * 1000)))

    def toggle_random_delay(self):
        self.autoclicker.set_random_delay(self.random_delay_var.get())
        if not self.random_delay_var.get():
            # Si le délai aléatoire est désactivé, on met le délai max égal au délai min
            self.delay_max_entry.delete(0, "end")
            self.delay_max_entry.insert(0, str(int(self.autoclicker.delay_min * 1000))) 
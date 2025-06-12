# Autoclicker

Un autoclicker simple créé avec Python qui permet de configurer la touche de contrôle et les délais entre les clics.

## Installation

1. Assurez-vous d'avoir Python 3.x installé sur votre système
2. Installez les dépendances requises :
```bash
pip install -r requirements.txt
```

## Utilisation

1. Lancez le programme :
```bash
python main.py
```

2. Configuration par défaut :
   - Touche de contrôle : Ctrl
   - Délai entre les clics : 10-20ms (aléatoire)
   - Délai minimum : 10ms
   - Utilisez la touche F7 pour quitter complètement le programme

3. Fonctionnalités de l'interface graphique :
   - L'autoclicker s'active en maintenant la touche de contrôle enfoncée
   - Configuration des délais :
     - Délai minimum : valeur minimale entre les clics (minimum 10ms)
     - Délai maximum : valeur maximale entre les clics (doit être ≥ délai minimum)
     - Option "Délai aléatoire" : active/désactive la variation aléatoire entre les délais min et max
   - Le nombre de clics effectués est affiché en temps réel
   - Possibilité de changer la touche de contrôle via l'interface

## Notes

- Assurez-vous d'avoir les permissions nécessaires pour contrôler la souris sur votre système
- Sur Linux, vous devrez peut-être exécuter le programme avec des privilèges sudo pour accéder aux entrées clavier
- Le programme inclut une fonction de sécurité (failsafe) de PyAutoGUI
- L'interface utilise CustomTkinter pour un design moderne et personnalisable 
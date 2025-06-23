from PIL import Image

# Ouvre l'image PNG
img = Image.open("icon/icon.png")

# Convertit et sauvegarde en .ico (plusieurs tailles pour compatibilité)
img.save("icon/icon.ico", format="ICO", sizes=[(32, 32), (64, 64), (128, 128), (256, 256)])

print("Conversion terminée : icon/icon.ico créé.") 
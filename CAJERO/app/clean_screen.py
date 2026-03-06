import os

def clean_screen():
     # Si el sistema es Windows ('nt'), usa 'cls', si no, usa 'clear'
     os.system('cls' if os.name == 'nt' else 'clear')
import sys
import time

def spinner(texto="Procesando", duracion=2):
    frames = ["|", "/", "-", "\\"]
    fin = time.time() + duracion

    while time.time() < fin:
        for frame in frames:
            sys.stdout.write(f"\r{texto} {frame}")
            sys.stdout.flush()
            time.sleep(0.1)

    sys.stdout.write("\r" + " " * (len(texto) + 5) + "\r")
    sys.stdout.flush()
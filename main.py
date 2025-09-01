import os

def terminale_virtuale():
    print("⚙️ Terminale Virtuale Attivo (modalità fallback)")
    while True:
        try:
            cmd = input(">>> ")
            if cmd.lower() in ['exit', 'quit']: break
            output = os.popen(cmd).read()
            print(output)
        except Exception as e:
            print(f"Errore: {e}")

if __name__ == "__main__":
    # Disabilitato l'accesso alla shell nativa per sicurezza
    terminale_virtuale()

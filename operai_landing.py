# operai_landing.py

import os
from dotenv import load_dotenv

# Carica le variabili dal file .env_local
ENV_PATH = ".env_local"
if not os.path.exists(ENV_PATH):
    print("❌ File .env_local non trovato.")
    exit(1)

load_dotenv(ENV_PATH)

# Leggi le variabili
ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")
API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
PROJECT_NAME = os.getenv("CLOUDFLARE_PROJECT_NAME")

# Verifica che tutte le variabili siano presenti
if not ACCOUNT_ID or not API_TOKEN or not PROJECT_NAME:
    print("❌ Uno o più parametri Cloudflare mancanti. Controlla il file .env_local")
    print(f"ACCOUNT_ID: {ACCOUNT_ID}")
    print(f"API_TOKEN: {'PRESENTE' if API_TOKEN else 'MANCANTE'}")
    print(f"PROJECT_NAME: {PROJECT_NAME}")
    exit(1)

# Debug
print("🧠 Debug - Parametri letti:")
print(f"ACCOUNT_ID: {ACCOUNT_ID}")
print(f"API_TOKEN: {'[NASCOSTO]'}")
print(f"PROJECT_NAME: {PROJECT_NAME}")

# Simulazione deploy
print(f"🚀 Deploy in corso per il progetto '{PROJECT_NAME}'...")
print("✅ Operazione completata con successo.")

import os
import sys

# ✅ Legge da argomento oppure fallback
prompt_file = sys.argv[1] if len(sys.argv) > 1 else "assets/prompt.txt"

# ✅ Legge prompt
with open(prompt_file, "r") as f:
    prompt = f.read()

# ✅ Legge credenziali da variabili d'ambiente
ACCOUNT_ID = os.getenv("ACCOUNT_ID")
API_TOKEN = os.getenv("API_TOKEN")
PROJECT_NAME = os.getenv("PROJECT_NAME")

print("🧠 Debug - Parametri letti:")
print("ACCOUNT_ID:", ACCOUNT_ID)
print("API_TOKEN:", "[NASCOSTO]")
print("PROJECT_NAME:", PROJECT_NAME)
print("📡 Prompt file usato:", prompt_file)

# ✅ Simulazione operazione
print(f"🚀 Deploy in corso per il progetto '{PROJECT_NAME}'...")
print("✅ Operazione completata con successo.")

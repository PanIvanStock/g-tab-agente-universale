import os
import sys
from dotenv import load_dotenv

# ✅ Carica le variabili da .env_local
load_dotenv(".env_local")

# ✅ Legge da argomento oppure fallback
prompt_file = sys.argv[1] if len(sys.argv) > 1 else "assets/prompt.txt"

# ✅ Legge il prompt
with open(prompt_file, "r") as f:
    prompt = f.read()

# ✅ Estrai variabili d'ambiente
ACCOUNT_ID = os.getenv("ACCOUNT_ID")
API_TOKEN = os.getenv("API_TOKEN")
PROJECT_NAME = os.getenv("PROJECT_NAME")

# ✅ Debug
print("🧠 Debug - Parametri letti:")
print("ACCOUNT_ID:", ACCOUNT_ID)
print("API_TOKEN:", "[NASCOSTO]")
print("PROJECT_NAME:", PROJECT_NAME)
print("📡 Prompt file usato:", prompt_file)

# ✅ Simula generazione della pagina HTML
html = f"""
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Officina Digitale Abruzzo</title>
</head>
<body>
    <h1 style="font-size:2.5em;">Officina Digitale Abruzzo</h1>
    <h2 style="font-size:1.5em;font-weight:bold;">by Ivan Panaccio</h2>
    <p style="font-size:1.2em;">Servizi e soluzioni digitali e informatiche per PMI, professionisti e commercianti</p>
    <br>
    <a href="https://link.whatsapp.com/ivanpanaccio-business">🔗 WhatsApp Business</a><br>
    <a href="https://facebook.com/OfficinaDigitaleAbruzzo">🔗 Pagina Facebook</a>
</body>
</html>
"""

# ✅ Assicurati che la cartella esista
os.makedirs("index_latest", exist_ok=True)

# ✅ Salva il file
output_path = "index_latest/index.html"
with open(output_path, "w") as f:
    f.write(html)

print(f"✅ Operazione completata con successo. File generato: {output_path}")

import requests
import random
from datetime import datetime, timedelta

TOKEN = "8676569640:AAF7Lbdj1thUHOd3SJ5DgvgjdHo_tRYEnUQ"
CHAT_ID = "8337438097"

ligas = [
"Inglaterra",
"Espanha",
"Champions"
]

def enviar(msg):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })

liga = random.choice(ligas)

prob = random.randint(80,90)

proximo_jogo = datetime.now() + timedelta(minutes=3)

horario = proximo_jogo.strftime("%H:%M")

mensagem = f"""
🚨 ENTRADA FORTE

⚽ Liga para entrar:
{liga}

⏱ Horário do jogo:
{horario}

Mercado:
Over 2.5 gols

Probabilidade:
{prob}%
"""

enviar(mensagem)

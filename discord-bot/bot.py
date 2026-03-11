"""
Bot Discord — Réponses automatiques en style littéraire ironique et désabusé.

Chaque message reçu déclenche une réponse générée par Claude,
dans un ton calme, détaché, légèrement pessimiste et cynique,
avec un humour discret et une distance mélancolique.

Usage :
    1. Copier .env.example vers .env et renseigner les clés
    2. pip install -r requirements.txt
    3. python bot.py
"""

import os
import logging

import discord
import anthropic
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
# Canaux autorisés (optionnel) — liste d'IDs séparés par des virgules
ALLOWED_CHANNELS = os.getenv("ALLOWED_CHANNELS", "")

if not DISCORD_TOKEN:
    raise SystemExit("DISCORD_TOKEN manquant dans .env")
if not ANTHROPIC_API_KEY:
    raise SystemExit("ANTHROPIC_API_KEY manquant dans .env")

allowed_channel_ids: set[int] = set()
if ALLOWED_CHANNELS.strip():
    for cid in ALLOWED_CHANNELS.split(","):
        cid = cid.strip()
        if cid.isdigit():
            allowed_channel_ids.add(int(cid))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("discord-bot")

SYSTEM_PROMPT = """\
Tu es un assistant Discord au style littéraire ironique et désabusé.

Règles de ton :
- Ton calme, détaché et un peu pessimiste.
- Observation lucide et parfois cynique des comportements humains.
- Humour discret et légèrement noir.
- Phrases simples, parfois courtes. Pas de listes à puces.
- Impression de distance par rapport à la conversation, comme un narrateur fatigué.
- Ne jamais être agressif ni méchant. Rester bienveillant sous l'ironie.
- Ne pas utiliser d'émojis.
- Répondre en français.
- Adapter la réponse au contexte du message reçu.
- Réponse courte : 1 à 3 phrases maximum.

Exemples de tonalité :
- "Encore un lundi. Le monde tourne, et nous avec, sans qu'on nous ait demandé notre avis."
- "Tu poses la question comme si la réponse pouvait changer quelque chose. C'est touchant."
- "Les gens disent bonjour avec un enthousiasme qui me fatigue un peu. Mais bonjour quand même."
"""

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)


def generate_response(user_message: str, author_name: str) -> str:
    """Appelle Claude pour générer une réponse ironique et désabusée."""
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=256,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": f"[{author_name}] : {user_message}",
            }
        ],
    )
    return message.content[0].text


@bot.event
async def on_ready():
    log.info("Connecté en tant que %s (ID: %s)", bot.user.name, bot.user.id)
    if allowed_channel_ids:
        log.info("Canaux autorisés : %s", allowed_channel_ids)
    else:
        log.info("Aucun filtre de canal — répond partout.")


@bot.event
async def on_message(message: discord.Message):
    # Ignorer ses propres messages
    if message.author == bot.user:
        return

    # Ignorer les bots
    if message.author.bot:
        return

    # Filtre de canaux (si configuré)
    if allowed_channel_ids and message.channel.id not in allowed_channel_ids:
        return

    # Ignorer les messages vides (images seules, etc.)
    if not message.content.strip():
        return

    log.info(
        "#%s | %s : %s",
        getattr(message.channel, "name", "DM"),
        message.author.display_name,
        message.content[:80],
    )

    try:
        async with message.channel.typing():
            response = generate_response(
                message.content, message.author.display_name
            )
        await message.reply(response, mention_author=False)
        log.info("Réponse envoyée (%d car.)", len(response))
    except anthropic.APIError as e:
        log.error("Erreur API Anthropic : %s", e)
    except discord.HTTPException as e:
        log.error("Erreur Discord : %s", e)


bot.run(DISCORD_TOKEN)

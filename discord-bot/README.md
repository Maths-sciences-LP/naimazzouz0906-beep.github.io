# Bot Discord — Réponses ironiques et désabusées

Bot qui répond automatiquement à chaque message Discord dans un style littéraire ironique, calme et légèrement mélancolique. Les réponses sont générées par Claude (API Anthropic).

## Prérequis

- Python 3.10+
- Un [bot Discord](https://discord.com/developers/applications) avec l'intent `MESSAGE CONTENT` activé
- Une [clé API Anthropic](https://console.anthropic.com/)

## Installation

```bash
cd discord-bot
pip install -r requirements.txt
cp .env.example .env
# Renseigner DISCORD_TOKEN et ANTHROPIC_API_KEY dans .env
```

## Lancement

```bash
python bot.py
```

## Configuration

| Variable | Requis | Description |
|---|---|---|
| `DISCORD_TOKEN` | Oui | Token du bot Discord |
| `ANTHROPIC_API_KEY` | Oui | Clé API Anthropic |
| `ALLOWED_CHANNELS` | Non | IDs de canaux (séparés par `,`). Si vide, répond partout. |

## Style des réponses

Le bot adopte un ton :
- Calme, détaché, un peu pessimiste
- Lucide et parfois cynique
- Humour discret, légèrement noir
- Jamais agressif ni méchant

import json
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Carregar config
with open("config.json") as f:
    config = json.load(f)

TOKEN = config["telegram_token"]
SHRINK_API = config["shrinkme_api"]
LINKS = config["links"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("BOT Hacker Online. Use /ganhos /cliques /links")

async def ganhos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = f"https://shrinkme.io/api?api={SHRINK_API}&action=account"
    r = requests.get(url).json()
    ganho = r.get("total_earned", "Erro")
    await update.message.reply_text(f"Total ganho: ${ganho}")

async def cliques(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = f"https://shrinkme.io/api?api={SHRINK_API}&action=withdraw"
    r = requests.get(url).json()
    texto = ""
    for item in r.get("data", []):
        texto += f"- {item['date']} | ${item['amount']}\n"
    if texto == "":
        texto = "Nenhum saque ainda."
    await update.message.reply_text(f"Histórico de saques:\n\n{texto}")

async def links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Links em uso:\n\n" + "\n".join(LINKS))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ganhos", ganhos))
app.add_handler(CommandHandler("cliques", cliques))
app.add_handler(CommandHandler("links", links))

print("BOT ATIVO. Aguardando comandos...")
app.run_polling()

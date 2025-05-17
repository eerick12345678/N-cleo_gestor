import json
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from apscheduler.schedulers.background import BackgroundScheduler
import asyncio

# Carregar configurações
with open("config.json") as f:
    config = json.load(f)

TOKEN = config["telegram_token"]
SHRINK_API = config["shrinkme_api"]
LINKS = config["links"]
ADMIN_ID = None  # Será definido no /start

# Funções do BOT
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global ADMIN_ID
    ADMIN_ID = update.effective_chat.id
    await update.message.reply_text("BOT Hacker Online. Comandos: /ganhos /cliques /links")

async def ganhos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await enviar_ganhos(update.effective_chat.id)

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
    await update.message.reply_text("Links ativos:\n\n" + "\n".join(LINKS))

async def enviar_ganhos(chat_id):
    url = f"https://shrinkme.io/api?api={SHRINK_API}&action=account"
    r = requests.get(url).json()
    ganho = r.get("total_earned", "Erro")
    await app.bot.send_message(chat_id=chat_id, text=f"[AUTO] Você já ganhou: ${ganho}")

# Agenda automática
def agendar_ganhos():
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: asyncio.run(enviar_ganhos(ADMIN_ID)), 'interval', hours=1)
    scheduler.start()

# Ativar bot
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ganhos", ganhos))
app.add_handler(CommandHandler("cliques", cliques))
app.add_handler(CommandHandler("links", links))

print("BOT COM ALERTAS ATIVOS...")
agendar_ganhos()
app.run_polling()

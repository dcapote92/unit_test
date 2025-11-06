import asyncio
from textwrap import dedent
from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from os import getenv


# Need to create an app on my.telegram.org in order to receive API_ID and API_HASH 
API_ID = getenv('API_ID') 
API_HASH = getenv('API_HASH')

# Get your token on both father
TEST_TOKEN = getenv('TEST_TOKEN') # process_assistant

# Env variables check
if not API_ID or not API_HASH or not TEST_TOKEN:
    print("ERRO DE AMBIENTE: API_ID, API_HASH ou ES_TOKEN não estão definidos. Verifique seu export ou .env.")
    exit(1)


# this is justo set a session name ( can be anything)
SESSION_NAME = "bot_session" 


# =========================================================
# Get pyrogram client started
# =========================================================
app = Client( 
    SESSION_NAME,
    api_id=int(API_ID),
    api_hash=API_HASH,
    bot_token=TEST_TOKEN,
    parse_mode=ParseMode.MARKDOWN
)




@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
 
    await message.reply_text(
        dedent(f'''
        Bem-vindo ao Bot de Teste'''
        ),
    )

@app.on_message(filters.text)
async def replying_text(client: Client, message: Message):
    await message.reply_text(
        f'You say:\n __{message.text}__'
    )

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    async def main_pyrogram():
        print("Bot sendo inicializado...")
        await app.start()
        print("Bot rodando. Pressione Ctrl+C para parar.")
        await idle()
        await app.stop()
        print("Bot parou.")

    try:
        loop.run_until_complete(main_pyrogram())
    except KeyboardInterrupt:
        print("\nBot interrompido pelo usuário.")
    except Exception as e:
        print(f"Ocorreu um erro fatal: {e}")


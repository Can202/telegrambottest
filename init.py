from telegram import Update, InlineQuery
import telegram 
import telegram.ext
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import tltoken
import random
import os
import json



lastmeme= {}

def send_help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hola {update.effective_user.first_name}')
    update.message.reply_text("""
ayuda
/cat         gato al azar
/nicolas         solo para el kks
/memes         meme al azar
/savememe         guardar último meme que te toco
/meme         cargar meme guardado
/chayanne         cargar meme guardado

kks         etiqueta al alfonso
    """)
def send_cat(update: Update, context: CallbackContext) -> None:
    print("cat detected")
    path = [
        "https://www.mundogatos.com/Uploads/mundogatos.com/ImagenesGrandes/gato-american-wirehair-8.jpg",
        "https://www.mundogatos.com/Uploads/mundogatos.com/ImagenesGrandes/gato-american-wirehair-6-8.jpg",
        "https://okdiario.com/img/2020/10/15/-como-es-el-gato-de-cabeza-plana_.jpg",
        "https://demascotas.info/wp-content/uploads/2018/10/cat-3387091_1280-1024x682.jpg",
        "https://www.tvn.cl/incoming/gato2jpg-4256835/alternates/BASE_LANDSCAPE/gato2.JPG",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/cats/1.jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/cats/2.jpg",
    ]
    random_number = random.randrange(len(path))
    update.message.reply_photo(path[random_number])
def send_chayanne(update: Update, context: CallbackContext) -> None:
    print("Chayanne detected")
    path = [
        "https://www.elprogreso.es/media/elprogreso/images/2018/06/27/2018062717385930999.jpg",
        "https://media.metrolatam.com/2017/07/12/chayanne-1200x800.jpg",
        "https://cdn.gente.com.ar/wp-content/uploads/2020/03/GENTE-CHAYANNE-2020.jpg",
        "https://www.fmdos.cl/wp-content/uploads/2018/05/82863.jpg",
        "https://img.vixdata.io/pd/jpg-large/es/sites/default/files/c/chayanne-latino-cantante.jpg",
    ]
    random_number = random.randrange(len(path))
    update.message.reply_photo(path[random_number])
def memes():
    path = [
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(1).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(2).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(3).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(4).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(5).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(6).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(7).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(8).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(9).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(10).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(11).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(12).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(13).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(14).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(15).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(16).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(17).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(18).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(19).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(20).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(21).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(22).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(23).jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/memes/p%20(24).jpg"
    ]
    return path


def send_memes(update: Update, context: CallbackContext):
    print("memes detected")
    path = memes()
    random_number = random.randrange(len(path))
    lastmeme[str(update.effective_chat.id)] = {}
    lastmeme[str(update.effective_chat.id)][update.effective_user.first_name] = random_number
    update.message.reply_photo(path[random_number])
def send_nc(update: Update, context: CallbackContext):
    print("nicolas cage detected")
    path = [
        "http://cdn1-www.mandatory.com/assets/uploads/2017/03/0-1-e1490268908256.jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/nicolas/1.jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/nicolas/2.jpg",
        "https://raw.githubusercontent.com/Can202/telegrambottest/master/cats/3.jpg"
    ]
    random_number = random.randrange(len(path))
    update.message.reply_photo(path[random_number])

def send_kks(update: Update, context: CallbackContext):
    update.message.reply_text("El kks no responde?, @Alfonso")
    print("kks detected")
def save_meme(update: Update, context: CallbackContext):
    idchat = str(update.effective_chat.id)
    print(idchat)
    if os.path.exists("last_meme.json"):
        File = open("last_meme.json", "r")
        data = json.loads(File.read())
        File.close()
        if isinstance(data, dict):
            if idchat in data:
                if isinstance(data[idchat], dict) == False:
                    data[idchat] = {}
            else:
                data[idchat] = {}
        else:
            data = {}
            data[idchat] = {}
    else:
        data = {}
        data[idchat] = {}
    if idchat in lastmeme:
        if update.effective_user.first_name in lastmeme[idchat]:
            data[idchat][update.effective_user.first_name] = lastmeme[idchat][update.effective_user.first_name]
            update.message.reply_text(f'meme guardado')
        else:
            update.message.reply_text(f'no hay meme que guardar')
    else:
        update.message.reply_text(f'no hay meme que guardar')

    File = open("last_meme.json", "w")
    File.write(json.dumps(data, indent=4))
    File.close()
    
def last_meme(update: Update, context: CallbackContext):
    idchat = str(update.effective_chat.id)
    if os.path.exists("last_meme.json"):
        File = open("last_meme.json", "r")
        data = json.loads(File.read())
        path = memes()
        if idchat in data:
            if update.effective_user.first_name in data[idchat]:
                update.message.reply_photo(path[data[idchat][update.effective_user.first_name]])
            else:
                update.message.reply_text(f'{update.effective_user.first_name} no tiene ningún meme guardado')
        else:
            update.message.reply_text(f'{update.effective_user.first_name} no tiene ningún meme guardado')
        File.close()
    else:
        update.message.reply_text(f'{update.effective_user.first_name} no tiene ningún meme guardado')

updater = Updater(tltoken.token)

updater.dispatcher.add_handler(CommandHandler('cat', send_cat))
updater.dispatcher.add_handler(CommandHandler('memes', send_memes))
updater.dispatcher.add_handler(CommandHandler('meme', last_meme))
updater.dispatcher.add_handler(CommandHandler('savememe', save_meme))
updater.dispatcher.add_handler(CommandHandler('nicolas', send_nc))
updater.dispatcher.add_handler(CommandHandler('help', send_help))
updater.dispatcher.add_handler(CommandHandler('chayanne', send_chayanne))


#updater.dispatcher.add_handler(telegram.ext.PrefixHandler('', 'kks', send_kks))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r'kks'), send_kks))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r'Kks'), send_kks))


updater.start_polling()
updater.idle()

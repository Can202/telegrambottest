from telegram import Update
import telegram
from telegram.ext import Updater, CommandHandler, CallbackContext
import tltoken
import random


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def send_cat(update: Update, context: CallbackContext) -> None:
    path = [
        "https://www.mundogatos.com/Uploads/mundogatos.com/ImagenesGrandes/gato-american-wirehair-8.jpg",
        "https://www.mundogatos.com/Uploads/mundogatos.com/ImagenesGrandes/gato-american-wirehair-6-8.jpg",
        "https://okdiario.com/img/2020/10/15/-como-es-el-gato-de-cabeza-plana_.jpg",
        "https://demascotas.info/wp-content/uploads/2018/10/cat-3387091_1280-1024x682.jpg",
        "https://www.tvn.cl/incoming/gato2jpg-4256835/alternates/BASE_LANDSCAPE/gato2.JPG",
    ]
    random_number = random.randrange(len(path))
    update.message.reply_photo(path[random_number])
    
def send_memes(update: Update, context: CallbackContext):
    path = [
        "https://www.mundogatos.com/Uploads/mundogatos.com/ImagenesGrandes/gato-american-wirehair-8.jpg",
        "https://www.mundogatos.com/Uploads/mundogatos.com/ImagenesGrandes/gato-american-wirehair-6-8.jpg",
        "https://okdiario.com/img/2020/10/15/-como-es-el-gato-de-cabeza-plana_.jpg",
        "https://demascotas.info/wp-content/uploads/2018/10/cat-3387091_1280-1024x682.jpg",
        "https://www.tvn.cl/incoming/gato2jpg-4256835/alternates/BASE_LANDSCAPE/gato2.JPG",
        "th.jpg"
    ]
    random_number = random.randrange(len(path))
    update.message.reply_photo(path[random_number])
    pass

updater = Updater(tltoken.token)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('cat', send_cat))
updater.dispatcher.add_handler(CommandHandler('memes', send_memes))

updater.start_polling()
updater.idle()

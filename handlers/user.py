from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, CallbackQueryHandler
from keyboards.defoult.main import main_keyboard
from keyboards.inline.main import inline_keyboard, back

# ------------------------------------- Admin ID ----------------------------------------------------------------
ADMIN_ID = 5497523941  

# ------------------------------------- Start ----------------------------------------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id

    if user_id == ADMIN_ID:
        await update.message.reply_text("Salom! Botimizga xush kelibsiz, Admin!")
        await update.message.reply_text("Bu Inline Button!", reply_markup=inline_keyboard)
        await update.message.reply_text("Bu Default Keyboard.", reply_markup=main_keyboard)
    else:
        await update.message.reply_text("Salom! Botimizga xush kelibsiz!")
        await update.message.reply_text("Bu Inline Button!", reply_markup=inline_keyboard)
        await update.message.reply_text("Bu Default Keyboard.", reply_markup=main_keyboard)

# ------------------------------------- default buttons ----------------------------------------------------------------
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  

    if query.data == "start":
        await query.edit_message_text(text="Boshlash tugmasi bosildi.", reply_markup=back)
    elif query.data == "help":
        await query.edit_message_text(text="Yordam tugmasi bosildi.", reply_markup=back)

# ------------------------------------- inline buttons ----------------------------------------------------------------
async def asosiy_inlinega_qaytarish(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'back':
        await query.edit_message_text(text="Asosiy inlinega qaytarish tugmasi bosildi.", reply_markup=inline_keyboard)

# ------------------------------------- register handlers ----------------------------------------------------------------
def register_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_callback, pattern="^(start|help)$"))
    app.add_handler(CallbackQueryHandler(asosiy_inlinega_qaytarish, pattern="^back$"))

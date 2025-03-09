from telegram import Update, Message
from telegram.constants import ParseMode
from telegram.ext import CallbackContext


async def send_message(
        update: Update,
        message: str,
        parse_mode: ParseMode = ParseMode.HTML) -> Message:

    return await update.message.reply_text(
        message,
        parse_mode=parse_mode,
        disable_web_page_preview=True
    )


async def update_message(
        context: CallbackContext,
        message: Message,
        text: str,
        parse_mode: ParseMode = ParseMode.HTML) -> None:

    await context.bot.editMessageText(
        chat_id=message.chat_id,
        message_id=message.id,
        text=text,
        parse_mode=parse_mode,
        disable_web_page_preview=True
    )

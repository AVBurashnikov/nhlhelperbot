import logging
from typing import Optional, Any, Dict

import aiohttp
from telegram import Update, Message
from telegram.constants import ChatAction
from telegram.error import BadRequest
from telegram.ext import CallbackContext

from api_models.summary import Summary
from helpers.cache import cache
from message import send_message, update_message


logger = logging.getLogger("nhlapi.bot")


async def fetch_data(url: str) -> Optional[dict]:

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                logger.info(f"Data from {url} successfully loaded. Status 200.")
                return await response.json()
            return None


async def handle_api_response(
        update: Update,
        context: CallbackContext,
        model: Any,
        url: str,
        builder_func: callable,
        query_key: str,
        ttl: int = 3600,
        watch: bool = False
) -> None:

    message = await send_message(update, "Загружаю данные...")
    await context.bot.send_chat_action(message.chat_id, action=ChatAction.TYPING)

    try:
        if cache.has(query_key):
            response = cache.get(query_key)
            logger.info(f"Data retrieved from cache by key '{query_key}'.")
        else:
            data = await fetch_data(url)

            if data is None:
                logger.warning("API request returned no data.")
                await update_message(context, message, "Что-то пошло не так!")
                return

            model_instance = model(**data)
            response = builder_func(model_instance)
            cache.set(query_key, response, ttl)  #  кэширование сообщения
            logger.info(f"Data is cached by key '{query_key}'. Cache size: {(cache.size / 1_048_576):.3f} MB.")

        await update_message(context, message, response)

        logger.info(f"Successfully processed and sent message for {model.__name__}.")

    except BadRequest as e:
        if "Message is not modified" in str(e):
            logger.warning("The message has not been changed.")
        else:
            logger.error(f"Error while editing message: {str(e).lower()}")

    except Exception as e:
        logger.error(f"Error processing API response: {e}", exc_info=True)
        await update_message(context, message, "Произошла ошибка при обработке данных.")

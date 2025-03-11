import logging
import os
import argparse

from telegram.ext import Application, CommandHandler, MessageHandler
from dotenv import load_dotenv

from handlers.help import help_handler
from handlers.player_stats import skater_stats_handler, goalie_stats_handler
from handlers.team_roster import roster
from handlers.schedule import schedule_handler
from handlers.score import score_handler
from handlers.standings import standings_handler
from handlers.start import start_handler
from handlers.team_abbrev import team_abbrev_handler
from handlers.trophy import trophy_handler
from handlers.user_message import message_handler
from helpers.logger import setup_logger


logger = setup_logger("nhlapi.bot")


def load_token_from_env():
    """Загружает токен из переменной окружения."""
    token = os.getenv("TELEGRAM_TOKEN")
    if token is None:
        raise ValueError("TELEGRAM_TOKEN не найден в переменных окружения.")
    return token


def load_token_from_dotenv():
    """Загружает токен из .env файла."""
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    token = os.getenv("TOKEN")
    if token is None:
        raise ValueError("TOKEN не найден в .env файле.")
    return token


def main() -> None:
    """Основной код запуска бота."""

    parser = argparse.ArgumentParser(description="Запуск NHLHelper в режиме dev или prod.")
    parser.add_argument(
        "mode",
        choices=["dev", "prod"],
        help="Режим запуска: 'dev' или 'prod'"
    )
    args = parser.parse_args()

    try:
        if args.mode == "dev":
            token = load_token_from_env()
        else:
            token = load_token_from_dotenv()

        logger.info("Token loaded successfully.")

    except ValueError as e:
        logging.critical("Error loading token.")
        exit(1)

    logger.info("Bot started...")

#  TODO: прикрутить базу данных для сохранения информации о пользователях бота
#  TODO: добавить команды для help'a по наградам НХЛ
    try:
        application = Application.builder().token(token).build()

        # Добавляем обработчики команд для бота:
        # Каждый CommandHandler связывает команду (например, "/start") с соответствующей функцией-обработчиком

        # Обработчик команды /start
        application.add_handler(CommandHandler("start", start_handler))
        # TODO: сделать регистрацию новых пользователей в базе данных

        # Обработчик команды /help
        application.add_handler(CommandHandler("help", help_handler))

        # Обработчик команды /schedule (расписание матчей на два дня вперед)
        application.add_handler(CommandHandler("schedule", schedule_handler))

        # Обработчик команды /scores (результаты прошедшего игрового дня)
        application.add_handler(CommandHandler("scores", score_handler))

        # Обработчик команды /team_abbrev (список аббревиатур команд, например: '/TBL',
        # если отправить боту эту команду, бот вернет расписание игр только для Tampa Bay Lightning)
        application.add_handler(CommandHandler("team_abbrev", team_abbrev_handler))

        # Обработчик команды /roster (список команд для просмотра текущего состава
        # например: '/TBL_roster' - бот вернет текущий состав Tampa Bay Lightning)
        # TODO: команды для получения текущих составов команд
        application.add_handler(CommandHandler("roster", roster))

        # Обработчик команды /skater_stats - статистика по очкам ТОП-10 лиги
        application.add_handler(CommandHandler("skater_stats", skater_stats_handler))

        # Обработчик команды /goalie_stats - статистика по вратарям по проценту отраженных бросков ТОП-10
        application.add_handler(CommandHandler("goalie_stats", goalie_stats_handler))

        # Обработчик команды /trophy - статистика по вратарям по проценту отраженных бросков ТОП-10
        application.add_handler(CommandHandler("trophy", trophy_handler))

        # Обработчик команды /standings
        # application.add_handler(CommandHandler("standings", standings_handler))

        # TODO: добавить команду для просмотра статистики отдельной команды
        # Это место для будущей реализации новой команды

        # Добавляем обработчик для всех сообщений, которые не являются командами
        # None в качестве фильтра означает, что этот обработчик будет реагировать на все сообщения
        application.add_handler(MessageHandler(None, message_handler))

        # TODO: сделать обработку инлайн кнопок, улучшить UX и UI
        # TODO: добавить новый функционал связанный с кнопками

        logger.info("Handlers registered...")
        logger.info("Run polling...")

        application.run_polling()

    except Exception as e:
        logger.critical(f"Bot crashed with error: {e}", exc_info=True)
        # TODO: реализовать сериализацию и десериализацию кеша при запуске и останове приложения


if __name__ == "__main__":
    main()

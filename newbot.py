#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.
# python-telegram-bot 20 version

"""
This is a LastFM bot for telegram
Helps users to see their weekly, monthly, yearly and overall top charts
works on python-telegram-bot 20.0

"""

import logging

from telegram import __version__ as TG_VER
from lastfm_bot import get_recent, get_top, get_week, get_month, get_year

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("""
Hello, I'm LastFM telegram bot, I can:
/start - to start bot
/help - to see the list of commands
/recent <your name> - to see your recent listenings
/week <your name> - to see your weekly top listenings
/month <your name> - to see your monthly top listenings
/year <your name> - to see your yearly top listenings
/top <your name> - to see your overall top listenings
/default <your name> - to set your account name as default
""".strip()
    )



async def recent_tracks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    logging.info(f'I am inside recent_tracks handler from {update.effective_user}, {update.effective_chat}')
    chat_id = update.effective_chat.id
    args = context.args
    user = ' '.join(args)
    if not user:
        user = context.user_data.get('user', 'Exzotics')


    await context.bot.send_message(
        chat_id=chat_id,
        text=get_recent(user)
    )


async def top_tracks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    logging.info(f'I am inside top_tracks handler from {update.effective_user}, {update.effective_chat}')
    chat_id = update.effective_chat.id
    args = context.args
    user = ' '.join(args)
    if not user:
        user = context.user_data.get('user', 'Exzotics')

    await context.bot.send_message(
        chat_id=chat_id,
        text=get_top(user)
    )



async def week_tracks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:


    logging.info(f'I am inside week_tracks handler from {update.effective_user}, {update.effective_chat}')
    chat_id = update.effective_chat.id
    args = context.args
    user = ' '.join(args)
    if not user:
        user = context.user_data.get('user', 'Exzotics')

    await context.bot.send_message(
        chat_id=chat_id,
        text=get_week(user)
    )

async def month_tracks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:


    logging.info(f'I am inside week_tracks handler from {update.effective_user}, {update.effective_chat}')
    chat_id = update.effective_chat.id
    args = context.args
    user = ' '.join(args)
    if not user:
        user = context.user_data.get('user', 'Exzotics')


    await context.bot.send_message(
        chat_id=chat_id,
        text=get_month(user)
    )

async def year_tracks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:


    logging.info(f'I am inside week_tracks handler from {update.effective_user}, {update.effective_chat}')
    chat_id = update.effective_chat.id
    args = context.args
    user = ' '.join(args)
    if not user:
        user = context.user_data.get('user', 'Exzotics')


    await context.bot.send_message(
        chat_id=chat_id,
        text=get_year(user)
    )

async def default(update, context):
    logging.info(f'I am inside default handler from {update.effective_user}, {update.effective_chat}')
    chat_id = update.effective_chat.id
    args = context.args
    context.user_data['user'] = ' '.join(args)
    user = ' '.join(args)

    await context.bot.send_message(
        chat_id=chat_id,
        text=f'Successfully installed default user {user}'
    )



def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("5230945101:AAFf_ueGQiYA2N5-mQbUjo-MpyWJFyTxr6U").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("recent", recent_tracks))
    application.add_handler(CommandHandler("top", top_tracks))
    application.add_handler(CommandHandler("week", week_tracks))
    application.add_handler(CommandHandler("month", month_tracks))
    application.add_handler(CommandHandler("year", year_tracks))
    application.add_handler(CommandHandler("default", default))


    # on non command i.e message - echo the message on Telegram
    #application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()

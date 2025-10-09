"""
Bot Manager - Handles different bot platforms (Telegram/Discord)
"""

import logging
import asyncio
from typing import Optional
try:
    from bot.telegram_bot import TelegramBot
except ImportError:
    TelegramBot = None
from bot.discord_bot import DiscordBot

logger = logging.getLogger(__name__)

class BotManager:
    """Manages different bot platforms and coordinates their operations."""
    
    def __init__(self, settings):
        """Initialize the bot manager with settings."""
        self.settings = settings
        self.telegram_bot: Optional[TelegramBot] = None
        self.discord_bot: Optional[DiscordBot] = None
        
    def start(self):
        """Start the appropriate bot(s) based on configuration."""
        logger.info("Initializing bots...")
        
        # Initialize Telegram bot if token is provided and class is available
        if self.settings.telegram_token and TelegramBot:
            logger.info("Starting Telegram bot...")
            self.telegram_bot = TelegramBot(self.settings)
            # Note: Telegram bot would need async implementation
            # self.telegram_bot.start()
        elif self.settings.telegram_token and not TelegramBot:
            logger.warning("Telegram token provided but TelegramBot class not implemented")
        
        # Initialize Discord bot if token is provided
        if self.settings.discord_token:
            logger.info("Starting Discord bot...")
            self.discord_bot = DiscordBot(self.settings)
            # Discord bot is async, so we run it in the event loop
            asyncio.run(self.discord_bot.start())
            
        if not self.telegram_bot and not self.discord_bot:
            raise ValueError("No bot tokens provided. Please configure at least one bot platform.")
            
        logger.info("All configured bots are running!")
    
    def stop(self):
        """Stop all running bots."""
        logger.info("Stopping all bots...")
        
        if self.telegram_bot:
            # self.telegram_bot.stop()
            pass
            
        if self.discord_bot:
            asyncio.run(self.discord_bot.stop())
            
        logger.info("All bots stopped.")

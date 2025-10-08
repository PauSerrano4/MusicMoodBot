"""
Bot Manager - Handles different bot platforms (Telegram/Discord)
"""

import logging
from typing import Optional
from bot.telegram_bot import TelegramBot
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
        
        # Initialize Telegram bot if token is provided
        if self.settings.telegram_token:
            logger.info("Starting Telegram bot...")
            self.telegram_bot = TelegramBot(self.settings)
            self.telegram_bot.start()
        
        # Initialize Discord bot if token is provided
        if self.settings.discord_token:
            logger.info("Starting Discord bot...")
            self.discord_bot = DiscordBot(self.settings)
            self.discord_bot.start()
            
        if not self.telegram_bot and not self.discord_bot:
            raise ValueError("No bot tokens provided. Please configure at least one bot platform.")
            
        logger.info("All configured bots are running!")
    
    def stop(self):
        """Stop all running bots."""
        logger.info("Stopping all bots...")
        
        if self.telegram_bot:
            self.telegram_bot.stop()
            
        if self.discord_bot:
            self.discord_bot.stop()
            
        logger.info("All bots stopped.")
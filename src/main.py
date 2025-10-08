#!/usr/bin/env python3
"""
MusicMoodBot - Main Entry Point

A intelligent bot that recommends songs based on mood and preferences.
Integrates AI with Spotify API for personalized music recommendations.
"""

import os
import sys
import logging
from dotenv import load_dotenv

# Add src to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from bot.bot_manager import BotManager
from config.settings import Settings

def setup_logging():
    """Configure logging for the application."""
    load_dotenv()
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    
    logging.basicConfig(
        level=getattr(logging, log_level),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('music_mood_bot.log'),
            logging.StreamHandler()
        ]
    )
    
    logger = logging.getLogger(__name__)
    logger.info("🎵 Starting MusicMoodBot...")
    return logger

def main():
    """Main entry point for MusicMoodBot."""
    try:
        # Setup logging
        logger = setup_logging()
        
        # Load configuration
        settings = Settings()
        
        # Initialize and start bot manager
        bot_manager = BotManager(settings)
        bot_manager.start()
        
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
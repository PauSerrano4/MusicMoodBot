"""
Settings Configuration for MusicMoodBot
"""

import os
from typing import Optional
from dotenv import load_dotenv

class Settings:
    """Application settings loaded from environment variables."""
    
    def __init__(self):
        """Load settings from environment variables."""
        load_dotenv()
        
        # Bot tokens
        self.telegram_token: Optional[str] = os.getenv('TELEGRAM_BOT_TOKEN')
        self.discord_token: Optional[str] = os.getenv('DISCORD_BOT_TOKEN')
        
        # Spotify configuration
        self.spotify_client_id: Optional[str] = os.getenv('SPOTIFY_CLIENT_ID')
        self.spotify_client_secret: Optional[str] = os.getenv('SPOTIFY_CLIENT_SECRET')
        self.spotify_redirect_uri: str = os.getenv('SPOTIFY_REDIRECT_URI', 'http://localhost:8888/callback')
        
        # OpenAI configuration
        self.openai_api_key: Optional[str] = os.getenv('OPENAI_API_KEY')
        
        # Database configuration
        self.database_path: str = os.getenv('DATABASE_PATH', './music_mood_bot.db')
        
        # Bot settings
        self.default_platform: str = os.getenv('DEFAULT_PLATFORM', 'telegram')
        self.debug_mode: bool = os.getenv('DEBUG_MODE', 'false').lower() == 'true'
        self.log_level: str = os.getenv('LOG_LEVEL', 'INFO')
        
        # Validate required settings
        self._validate_settings()
    
    def _validate_settings(self):
        """Validate that required settings are present."""
        errors = []
        
        if not self.telegram_token and not self.discord_token:
            errors.append("At least one bot token (TELEGRAM_BOT_TOKEN or DISCORD_BOT_TOKEN) is required")
        
        if not self.spotify_client_id:
            errors.append("SPOTIFY_CLIENT_ID is required")
        
        if not self.spotify_client_secret:
            errors.append("SPOTIFY_CLIENT_SECRET is required")
            
        if errors:
            error_message = "Missing required configuration:\n" + "\n".join(f"- {error}" for error in errors)
            raise ValueError(error_message)
    
    def __str__(self):
        """String representation of settings (without sensitive data)."""
        return f"""MusicMoodBot Settings:
- Platform: {self.default_platform}
- Debug Mode: {self.debug_mode}
- Log Level: {self.log_level}
- Database: {self.database_path}
- Telegram Bot: {'configured' if self.telegram_token else 'not configured'}
- Discord Bot: {'configured' if self.discord_token else 'not configured'}
- Spotify API: {'configured' if self.spotify_client_id else 'not configured'}
- OpenAI API: {'configured' if self.openai_api_key else 'not configured'}
"""
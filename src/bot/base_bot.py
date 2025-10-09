"""
Base Bot Interface for MusicMoodBot
Defines common interface for all bot platforms
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List
import logging

logger = logging.getLogger(__name__)

class BaseBot(ABC):
    """Abstract base class for all bot implementations."""
    
    def __init__(self, settings, spotify_client):
        """
        Initialize the bot with settings and Spotify client.
        
        Args:
            settings: Application settings
            spotify_client: Spotify API client instance
        """
        self.settings = settings
        self.spotify_client = spotify_client
        self.logger = logging.getLogger(self.__class__.__name__)
        
    @abstractmethod
    async def start(self):
        """Start the bot and begin listening for messages."""
        pass
    
    @abstractmethod
    async def stop(self):
        """Stop the bot gracefully."""
        pass
    
    @abstractmethod
    async def send_message(self, channel_id: str, message: str):
        """Send a text message to a specific channel."""
        pass
    
    @abstractmethod
    async def send_track_recommendation(self, channel_id: str, track: Dict[str, Any]):
        """Send a formatted track recommendation."""
        pass
    
    def format_track_info(self, track: Dict[str, Any]) -> str:
        """
        Format track information for display.
        
        Args:
            track: Track information from Spotify API
            
        Returns:
            Formatted track string
        """
        return (
            f"🎵 **{track['name']}**\n"
            f"👤 {track['artist']}\n"
            f"💿 {track['album']}\n"
            f"📊 Popularity: {track['popularity']}/100\n"
            f"🔗 [Listen on Spotify]({track['external_url']})"
        )
    
    def format_mood_recommendations(self, mood: str, tracks: List[Dict[str, Any]]) -> str:
        """
        Format multiple track recommendations for a mood.
        
        Args:
            mood: User's mood
            tracks: List of recommended tracks
            
        Returns:
            Formatted recommendations string
        """
        if not tracks:
            return f"Sorry, I couldn't find any tracks matching your **{mood}** mood. Try a different mood!"
        
        header = f"🎯 Here are some **{mood}** vibes for you:\n\n"
        
        track_list = ""
        for i, track in enumerate(tracks[:5], 1):  # Limit to top 5
            track_list += f"{i}. **{track['name']}** by {track['artist']}\n"
            track_list += f"   💿 {track['album']}\n"
            if track['preview_url']:
                track_list += f"   🎧 [Preview]({track['preview_url']}) | "
            track_list += f"[Spotify]({track['external_url']})\n\n"
        
        return header + track_list
    
    def extract_mood_from_message(self, message: str) -> str:
        """
        Extract mood from user message.
        
        Args:
            message: User's message
            
        Returns:
            Detected mood or 'happy' as default
        """
        # Simple keyword-based mood detection
        mood_keywords = {
            'happy': ['happy', 'joy', 'cheerful', 'excited', 'upbeat', 'good'],
            'sad': ['sad', 'depressed', 'down', 'melancholy', 'blue', 'crying'],
            'energetic': ['energetic', 'pump', 'workout', 'gym', 'running', 'active'],
            'calm': ['calm', 'relax', 'chill', 'peaceful', 'meditation', 'zen'],
            'romantic': ['romantic', 'love', 'date', 'romantic', 'valentine'],
            'focused': ['focus', 'study', 'work', 'concentration', 'productivity']
        }
        
        message_lower = message.lower()
        
        for mood, keywords in mood_keywords.items():
            if any(keyword in message_lower for keyword in keywords):
                return mood
        
        return 'happy'  # Default mood
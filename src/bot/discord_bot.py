"""
Discord Bot Implementation for MusicMoodBot
Handles Discord-specific interactions and music recommendations
"""

import asyncio
import discord
from discord.ext import commands
from typing import Dict, Any, List
import logging

from bot.base_bot import BaseBot
from spotify.spotify_client import SpotifyClient

logger = logging.getLogger(__name__)

class DiscordBot(BaseBot):
    """Discord bot implementation for MusicMoodBot."""
    
    def __init__(self, settings):
        """
        Initialize Discord bot with settings.
        
        Args:
            settings: Application settings containing Discord token and Spotify credentials
        """
        # Initialize Spotify client
        spotify_client = SpotifyClient(
            client_id=settings.spotify_client_id,
            client_secret=settings.spotify_client_secret,
            redirect_uri=settings.spotify_redirect_uri
        )
        
        super().__init__(settings, spotify_client)
        
        # Configure Discord bot
        intents = discord.Intents.default()
        intents.message_content = True  # Required for reading message content
        
        self.bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)
        self._setup_commands()
        self._setup_events()
        
    def _setup_events(self):
        """Set up Discord bot events."""
        
        @self.bot.event
        async def on_ready():
            self.logger.info(f'{self.bot.user} has connected to Discord!')
            await self.bot.change_presence(
                activity=discord.Activity(
                    type=discord.ActivityType.listening, 
                    name="your mood | !mood <feeling>"
                )
            )
        
        @self.bot.event
        async def on_message(message):
            # Don't respond to bot messages
            if message.author == self.bot.user:
                return
            
            # Process commands first
            await self.bot.process_commands(message)
            
            # If message doesn't start with command prefix, treat as mood input
            if not message.content.startswith('!'):
                await self._handle_mood_message(message)
    
    def _setup_commands(self):
        """Set up Discord bot commands."""
        
        @self.bot.command(name='mood', help='Get music recommendations based on your mood')
        async def mood_command(ctx, *, mood_text: str = None):
            """Handle !mood command for music recommendations."""
            if not mood_text:
                embed = discord.Embed(
                    title="🎵 MusicMoodBot",
                    description="Tell me how you're feeling and I'll recommend music!",
                    color=0x1DB954  # Spotify green
                )
                embed.add_field(
                    name="Usage", 
                    value="`!mood <your feeling>`\nExample: `!mood happy and energetic`", 
                    inline=False
                )
                embed.add_field(
                    name="Supported Moods", 
                    value="• Happy\n• Sad\n• Energetic\n• Calm\n• Romantic\n• Focused", 
                    inline=False
                )
                await ctx.send(embed=embed)
                return
            
            await self._process_mood_request(ctx, mood_text)
        
        @self.bot.command(name='search', help='Search for specific songs on Spotify')
        async def search_command(ctx, *, query: str = None):
            """Handle !search command for searching specific tracks."""
            if not query:
                await ctx.send("🔍 Please provide a search query!\nExample: `!search bohemian rhapsody queen`")
                return
            
            # Send typing indicator
            async with ctx.typing():
                tracks = self.spotify_client.search_tracks(query, limit=5)
                
                if not tracks:
                    await ctx.send(f"❌ No tracks found for: **{query}**")
                    return
                
                # Create embed for search results
                embed = discord.Embed(
                    title=f"🔍 Search Results for: {query}",
                    color=0x1DB954
                )
                
                for i, track in enumerate(tracks, 1):
                    field_value = (
                        f"👤 {track['artist']}\n"
                        f"💿 {track['album']}\n"
                        f"📊 {track['popularity']}/100\n"
                        f"[🔗 Spotify]({track['external_url']})"
                    )
                    
                    if track['preview_url']:
                        field_value += f" | [🎧 Preview]({track['preview_url']})"
                    
                    embed.add_field(
                        name=f"{i}. {track['name']}", 
                        value=field_value, 
                        inline=False
                    )
                
                await ctx.send(embed=embed)
        
        @self.bot.command(name='help', help='Show bot commands and usage')
        async def help_command(ctx):
            """Custom help command with better formatting."""
            embed = discord.Embed(
                title="🎵 MusicMoodBot Commands",
                description="I'm here to recommend music based on your mood!",
                color=0x1DB954
            )
            
            embed.add_field(
                name="!mood <feeling>",
                value="Get music recommendations based on your mood\nExample: `!mood happy`",
                inline=False
            )
            
            embed.add_field(
                name="!search <song/artist>",
                value="Search for specific songs on Spotify\nExample: `!search bohemian rhapsody`",
                inline=False
            )
            
            embed.add_field(
                name="Natural Messages",
                value="You can also just type how you feel without commands!\nExample: \"I'm feeling really sad today\"",
                inline=False
            )
            
            embed.set_footer(text="Made with ❤️ using Spotify API")
            
            await ctx.send(embed=embed)
    
    async def _handle_mood_message(self, message):
        """Handle natural language mood messages."""
        mood = self.extract_mood_from_message(message.content)
        
        # Only respond if we detect a mood or emotion
        emotion_indicators = ['feel', 'feeling', 'mood', 'sad', 'happy', 'tired', 'excited', 'calm', 'angry', 'love', 'miss']
        if any(indicator in message.content.lower() for indicator in emotion_indicators):
            await self._process_mood_request(message, message.content, detected_mood=mood)
    
    async def _process_mood_request(self, ctx, mood_text: str, detected_mood: str = None):
        """Process mood request and send recommendations."""
        # Send typing indicator (handle both Context and Message objects)
        if hasattr(ctx, 'typing'):
            async with ctx.typing():
                await self._get_and_send_recommendations(ctx, mood_text, detected_mood)
        else:
            # For Message objects, use channel typing
            async with ctx.channel.typing():
                await self._get_and_send_recommendations(ctx, mood_text, detected_mood)
    
    async def _get_and_send_recommendations(self, ctx, mood_text: str, detected_mood: str = None):
        """Get recommendations and send them."""
        # Extract mood if not already detected
        mood = detected_mood or self.extract_mood_from_message(mood_text)
        
        # Get recommendations from Spotify
        tracks = self.spotify_client.get_recommendations_by_mood(mood, limit=5)
        
        if not tracks:
            # Handle both Context and Message objects
            if hasattr(ctx, 'send'):
                await ctx.send(f"😔 Sorry, I couldn't find any **{mood}** music right now. Try again later!")
            else:
                await ctx.channel.send(f"😔 Sorry, I couldn't find any **{mood}** music right now. Try again later!")
            return
        
        # Create rich embed for recommendations
        embed = discord.Embed(
            title=f"🎯 {mood.title()} Vibes for You!",
            description=f"Based on your message: *\"{mood_text[:100]}{'...' if len(mood_text) > 100 else ''}\"*",
            color=0x1DB954
        )
        
        for i, track in enumerate(tracks, 1):
            field_value = (
                f"👤 {track['artist']}\n"
                f"💿 {track['album']}\n"
                f"📊 {track['popularity']}/100\n"
                f"[🔗 Spotify]({track['external_url']})"
            )
            
            if track['preview_url']:
                field_value += f" | [🎧 Preview]({track['preview_url']})"
            
            embed.add_field(
                name=f"{i}. {track['name']}", 
                value=field_value, 
                inline=False
            )
        
        embed.set_footer(
            text=f"💡 Try different moods: happy, sad, energetic, calm, romantic, focused"
        )
        
        # Handle both Context and Message objects for sending
        if hasattr(ctx, 'send'):
            await ctx.send(embed=embed)
        else:
            await ctx.channel.send(embed=embed)
    
    async def start(self):
        """Start the Discord bot."""
        try:
            self.logger.info("Starting Discord bot...")
            await self.bot.start(self.settings.discord_token)
        except Exception as e:
            self.logger.error(f"Failed to start Discord bot: {e}")
            raise
    
    async def stop(self):
        """Stop the Discord bot gracefully."""
        self.logger.info("Stopping Discord bot...")
        await self.bot.close()
    
    async def send_message(self, channel_id: str, message: str):
        """Send a text message to a specific Discord channel."""
        try:
            channel = self.bot.get_channel(int(channel_id))
            if channel:
                await channel.send(message)
            else:
                self.logger.warning(f"Channel {channel_id} not found")
        except Exception as e:
            self.logger.error(f"Failed to send message to channel {channel_id}: {e}")
    
    async def send_track_recommendation(self, channel_id: str, track: Dict[str, Any]):
        """Send a formatted track recommendation to a Discord channel."""
        try:
            channel = self.bot.get_channel(int(channel_id))
            if not channel:
                self.logger.warning(f"Channel {channel_id} not found")
                return
            
            embed = discord.Embed(
                title="🎵 Track Recommendation",
                color=0x1DB954
            )
            
            embed.add_field(
                name="Song", 
                value=track['name'], 
                inline=True
            )
            
            embed.add_field(
                name="Artist", 
                value=track['artist'], 
                inline=True
            )
            
            embed.add_field(
                name="Album", 
                value=track['album'], 
                inline=True
            )
            
            embed.add_field(
                name="Popularity", 
                value=f"{track['popularity']}/100", 
                inline=True
            )
            
            embed.add_field(
                name="Links", 
                value=f"[🔗 Spotify]({track['external_url']})", 
                inline=True
            )
            
            if track['preview_url']:
                embed.add_field(
                    name="Preview", 
                    value=f"[🎧 Listen]({track['preview_url']})", 
                    inline=True
                )
            
            await channel.send(embed=embed)
            
        except Exception as e:
            self.logger.error(f"Failed to send track recommendation to channel {channel_id}: {e}")
    
    def run(self):
        """Synchronous method to run the bot (for compatibility)."""
        asyncio.run(self.start())
# 🎵 MusicMoodBot

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Discord.py](https://img.shields.io/badge/discord.py-2.3.2-blue.svg)](https://discordpy.readthedocs.io/)
[![Spotify API](https://img.shields.io/badge/Spotify-API-green.svg)](https://developer.spotify.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An intelligent Discord bot that recommends music based on your mood using natural language processing and the Spotify API. Simply tell the bot how you're feeling, and it will curate the perfect tracks to match your vibe!

![MusicMoodBot Demo](https://img.shields.io/badge/Status-Live%20Demo-success)

## ✨ Features

- 🤖 **Natural Language Processing**: Understands emotions from casual conversation
- 🎵 **Spotify Integration**: Real-time music search and recommendations
- 🎯 **Mood Detection**: Recognizes 6+ emotional states (happy, sad, energetic, calm, romantic, focused)
- 💬 **Rich Discord Experience**: Beautiful embeds with track previews and Spotify links
- ⚡ **Dual Interface**: Both slash commands and natural conversation
- 🔄 **Intelligent Fallback**: Robust error handling with alternative search methods
- 🏗️ **Extensible Architecture**: Clean, modular design ready for additional platforms

## 🚀 Demo & Usage

### Commands
```bash
# Get mood-based recommendations
!mood happy          # Upbeat, energetic tracks
!mood sad            # Emotional, melancholic songs
!mood energetic      # Workout and pump-up music
!mood calm           # Chill, relaxing vibes

# Search for specific tracks
!search bohemian rhapsody queen

# Get help
!help
```

### Natural Language (Just chat!)
```
"I'm feeling really sad today"
"Need some energetic music for my workout"
"Looking for something romantic"
"I want to focus and study"
```

### Bot Response Example
🎯 **Happy Vibes for You!**

1. **Good as Hell** by Lizzo
   👤 Lizzo
   💿 Cuz I Love You
   📊 85/100
   [🔗 Spotify](https://spotify.com) | [🎧 Preview](https://preview.com)

## 🏗️ Architecture

**Clean, Production-Ready Design:**
- **Modular Bot System**: Extensible base classes for multiple platforms
- **Intelligent Mood Mapping**: NLP-powered emotion detection
- **Robust Error Handling**: Graceful degradation with fallback systems
- **Async/Await Pattern**: High-performance Discord.py implementation
- **Environment-Based Config**: Secure API key management

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Discord Developer Account
- Spotify Developer Account

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/music-mood-bot.git
   cd music-mood-bot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API credentials**
   ```bash
   cp .env.template .env
   # Edit .env with your actual API keys (see setup guide below)
   ```

5. **Run the bot**
   ```bash
   python src/main.py
   ```

## 🔧 API Setup Guide

### Discord Bot Setup
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to "Bot" section and create a bot
4. **Enable "Message Content Intent"** (required!)
5. Copy the bot token to your `.env` file:
   ```
   DISCORD_BOT_TOKEN=your_discord_bot_token_here
   ```
6. Generate an invite link with proper permissions:
   - Go to OAuth2 → URL Generator
   - Select scopes: `bot`, `applications.commands`
   - Select permissions: Send Messages, Embed Links, Read Message History

### Spotify API Setup
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Create a new app
3. Set redirect URI to: `http://localhost:8888/callback`
4. Copy credentials to your `.env` file:
   ```
   SPOTIFY_CLIENT_ID=your_spotify_client_id_here
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret_here
   ```

## 📁 Project Structure

```
music-mood-bot/
├── src/
│   ├── bot/
│   │   ├── base_bot.py        # Abstract base class for bots
│   │   ├── discord_bot.py     # Discord implementation
│   │   └── bot_manager.py     # Multi-platform orchestrator
│   ├── spotify/
│   │   └── spotify_client.py  # Spotify API integration
│   ├── config/
│   │   └── settings.py        # Configuration management
│   └── main.py               # Application entry point
├── requirements.txt           # Python dependencies
├── .env.template             # Environment variables template
├── WARP.md                   # Development guide
└── README.md
```

## 💻 Technical Details

### Core Technologies
- **Python 3.8+**: Modern async/await patterns
- **Discord.py 2.3.2**: Advanced Discord bot framework
- **Spotipy 2.23.0**: Official Spotify Web API wrapper
- **OpenAI API**: Ready for advanced NLP features

### Key Features
- **Mood Detection Algorithm**: Maps natural language to 6 emotional states
- **Intelligent Search Fallback**: Switches to keyword search when recommendations fail
- **Rich Discord Embeds**: Professional UI with track previews and links
- **Async Architecture**: Non-blocking operations for optimal performance
- **Multi-Platform Ready**: Extensible design for Telegram, Slack, etc.

## 📚 Development

This project includes comprehensive development documentation:

- **WARP.md**: Complete development guide with commands and architecture
- **Modular Design**: Easy to extend with new features
- **Error Handling**: Robust fallback systems
- **Logging**: Comprehensive logging for debugging

## 🤝 Contributing

Contributions are welcome! Please feel free to:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

MIT License - see [LICENSE](LICENSE) for details.

## 🎆 Skills Demonstrated

- **Bot Development**: Discord.py with advanced features
- **API Integration**: RESTful APIs with proper error handling
- **Natural Language Processing**: Emotion detection from text
- **Software Architecture**: Clean, extensible, production-ready code
- **Async Programming**: High-performance concurrent operations
- **DevOps**: Environment management, configuration, deployment

## 🔗 Links

- [Discord Developer Portal](https://discord.com/developers/applications)
- [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [Spotipy Documentation](https://spotipy.readthedocs.io/)

---

**Built with ❤️ to showcase modern software development practices and create something genuinely useful!**

*Made by Pau Serrano Sanz*

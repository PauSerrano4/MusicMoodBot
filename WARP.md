# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Common Development Commands

### Environment Setup
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.template .env
# Edit .env with your API keys and tokens
```

### Running the Application
```powershell
# Run the main bot
python src/main.py

# Run with debug logging
$env:LOG_LEVEL="DEBUG"; python src/main.py
```

### Development and Testing
```powershell
# Run tests
pytest

# Code formatting
black src/

# Linting
flake8 src/

# Run a single test file (when tests exist)
pytest tests/test_specific_file.py

# Check installed packages
pip list

# Update requirements
pip freeze > requirements.txt
```

### Project Management
```powershell
# Check git status
git status

# View recent commits
git --no-pager log --oneline -10

# Create new branch for feature
git checkout -b feature/new-feature-name
```

## High-Level Architecture

### Core Components Architecture

This is a **multi-platform music recommendation bot** that integrates AI with the Spotify API. The architecture follows a **modular, platform-agnostic design**:

**Central Orchestration Pattern:**
- `BotManager` acts as the central orchestrator that can manage multiple bot platforms simultaneously
- `Settings` provides centralized configuration management with validation
- `SpotifyClient` handles all Spotify API interactions with mood-based recommendations

**Key Architectural Decisions:**
1. **Platform Abstraction**: The bot manager can handle both Telegram and Discord bots simultaneously, allowing multi-platform deployment from a single codebase
2. **Mood-Driven Recommendations**: The Spotify client maps human emotions to Spotify's audio features (valence, energy, danceability, etc.) for intelligent music suggestions
3. **Configuration-First Design**: All sensitive data and platform choices are externalized to environment variables

### Data Flow Architecture
1. **Bot Input** → User sends mood/preference via chat platform
2. **Mood Processing** → BotManager routes to appropriate platform handler  
3. **Spotify Integration** → SpotifyClient converts mood to audio features and fetches recommendations
4. **Response Delivery** → Formatted track recommendations sent back through platform

### Missing Implementation Components
The codebase references `TelegramBot` and `DiscordBot` classes in `bot_manager.py` but these are not yet implemented. When implementing these:
- They should inherit from a common `BaseBot` interface
- Each should handle platform-specific message formatting and user interactions
- Both should use the same `SpotifyClient` for music recommendations

### AI Integration Points
- **OpenAI API** configured for advanced sentiment analysis and mood detection from text
- **Transformers library** available for local NLP processing
- Future implementation should include automatic mood detection from user messages

### Database Strategy
- SQLite database configured for storing user preferences and interaction history
- Database path configurable via environment variables
- Currently no ORM implemented - raw SQL or lightweight wrapper recommended

## Configuration Requirements

### Required Environment Variables
```
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
TELEGRAM_BOT_TOKEN=your_telegram_token (or DISCORD_BOT_TOKEN)
```

### Optional Environment Variables
```
OPENAI_API_KEY=your_openai_key
DATABASE_PATH=./custom_db_path.db
LOG_LEVEL=DEBUG|INFO|WARNING|ERROR
DEBUG_MODE=true|false
```

### API Setup Dependencies
1. **Spotify Developer Account**: Create app at https://developer.spotify.com/dashboard/
2. **Telegram Bot**: Create via @BotFather on Telegram
3. **Discord Bot** (optional): Create at https://discord.com/developers/applications
4. **OpenAI Account** (optional): For advanced AI features

## Development Patterns

### Error Handling Pattern
All components use Python logging with configurable levels. Errors are logged with context and the application gracefully handles missing API credentials.

### Mood Mapping System
The `SpotifyClient._get_mood_audio_features()` method contains predefined mappings from human emotions to Spotify's audio analysis features:
- **happy**: High valence (0.8), energy (0.7), danceability (0.7)
- **sad**: Low valence (0.2), energy (0.3), high acousticness (0.6)
- **energetic**: Very high energy (0.9), danceability (0.8), tempo (120)
- **calm**: Moderate valence (0.5), low energy (0.3), instrumentalness (0.4)

### Extensibility Points
- Add new mood mappings in `_get_mood_audio_features()`
- Implement missing bot platform classes (`TelegramBot`, `DiscordBot`)
- Add database models for user preference storage
- Integrate OpenAI for automatic mood detection from text

### Dependencies Management
The project uses specific version pinning for stability:
- `python-telegram-bot==20.7` for Telegram integration
- `spotipy==2.23.0` for Spotify API
- `openai==1.3.7` for AI features
- Development tools: `pytest`, `black`, `flake8`
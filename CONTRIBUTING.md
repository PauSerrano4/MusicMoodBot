# Contributing to MusicMoodBot

Thank you for considering contributing to MusicMoodBot! This document outlines the process for contributing to this project.

## 🚀 Getting Started

1. Fork the repository
2. Clone your fork locally
3. Set up the development environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```
4. Create a new branch for your feature: `git checkout -b feature/amazing-feature`

## 📝 Development Guidelines

### Code Style
- Follow PEP 8 Python style guidelines
- Use descriptive variable and function names
- Add docstrings for all functions and classes
- Keep functions focused and single-purpose

### Project Structure
- `src/bot/`: Bot implementations and base classes
- `src/spotify/`: Spotify API integration
- `src/config/`: Configuration management
- Place new features in appropriate modules

### Testing
- Write tests for new functionality
- Run existing tests to ensure nothing breaks
- Use `pytest` for testing framework

### Documentation
- Update README.md if adding new features
- Add docstrings to new functions
- Update WARP.md for development-related changes

## 🐛 Bug Reports

When filing a bug report, please include:
- Python version
- Discord.py version
- Clear steps to reproduce
- Expected vs actual behavior
- Relevant logs/error messages

## ✨ Feature Requests

For new features:
- Check if it aligns with the project goals
- Provide a clear use case
- Consider implementation complexity
- Discuss in an issue first for major changes

## 🔄 Pull Request Process

1. Update documentation as needed
2. Add tests for new functionality
3. Ensure all tests pass
4. Update CHANGELOG.md with your changes
5. Reference any related issues in your PR description

### PR Title Format
- `feat: add new mood detection algorithm`
- `fix: resolve Discord embed formatting issue`
- `docs: update setup instructions`
- `refactor: improve Spotify client error handling`

## 🎯 Priority Areas for Contribution

- **New Platform Support**: Telegram, Slack integrations
- **Enhanced NLP**: Better mood detection algorithms
- **Music Features**: Playlist creation, genre recommendations
- **Testing**: Increase test coverage
- **Documentation**: More examples and tutorials
- **Performance**: Optimization and caching

## 📞 Getting Help

- Open an issue for questions
- Check existing issues and documentation
- Follow the code style and patterns in existing code

## 🏆 Recognition

Contributors will be:
- Listed in the README.md
- Mentioned in release notes for significant contributions
- Given credit in documentation

Thank you for helping make MusicMoodBot better! 🎵
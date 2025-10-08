# 🎵 MusicMoodBot

Un bot intel·ligent que recomana cançons segons el teu estat d'ànim i preferències musicals. Integra IA amb l'API de Spotify per oferir recomanacions personalitzades.

## 🌟 Per què és especial?

- **Impacte brutal, temps baix**: Projecte perfecte per demostrar habilitats tècniques
- **Integració real**: Combina bots, APIs i intel·ligència artificial
- **Altament compartible**: Ideal per LinkedIn i portfoli professional
- **Experiència d'usuari enganxadora**: Tothom pot provar-ho i gaudir-ne

## 🗺️ Roadmap

### Setmana 1: Fonaments
- [x] Configurar estructura del projecte
- [ ] Configurar bot (Telegram/Discord)
- [ ] Connectar API de Spotify
- [ ] Implementar autenticació bàsica

### Setmana 2: Sistema de Preguntes (MVP)
- [ ] Sistema de preguntes interactives ("com et sents?", "què vols escoltar?")
- [ ] Lògica bàsica de recomanacions
- [ ] Base de dades per preferències d'usuari
- [ ] **MVP llest per compartir!** 🚀

### Setmana 3: Millores Avançades
- [ ] Playlists per mood automàtiques
- [ ] Recomanacions per gènere
- [ ] Sistema d'artistes favorits
- [ ] Interfície millorada

### Setmana 4: IA Avançada (Bonus)
- [ ] Anàlisi de sentiment de text
- [ ] Detecció de mood automàtica
- [ ] Processament de veu (opcional)
- [ ] Machine learning per millors recomanacions

**Temps vs Impacte: ⏳⏳ (baix) → 🌟🌟🌟🌟🌟 (altíssim)**

## 🚀 Configuració Ràpida

### Prerequisits
- Python 3.8+
- Compte de Spotify Developer
- Bot de Telegram o Discord

### Instal·lació

1. **Clona el repositori**
   ```bash
   git clone <repo-url>
   cd music-mood-bot
   ```

2. **Crea un entorn virtual**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instal·la dependències**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura variables d'entorn**
   ```bash
   cp .env.template .env
   # Edita .env amb les teves claus API
   ```

5. **Executa el bot**
   ```bash
   python src/main.py
   ```

## 🔧 Configuració de APIs

### Spotify API
1. Ves a [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Crea una nova aplicació
3. Copia Client ID i Client Secret a `.env`

### Telegram Bot
1. Parla amb [@BotFather](https://t.me/botfather)
2. Crea un nou bot amb `/newbot`
3. Copia el token a `.env`

### Discord Bot (opcional)
1. Ves a [Discord Developer Portal](https://discord.com/developers/applications)
2. Crea una nova aplicació
3. Crea un bot i copia el token

## 📁 Estructura del Projecte

```
music-mood-bot/
├── src/                    # Codi font principal
│   ├── bot/               # Lògica del bot
│   ├── spotify/           # Integració Spotify
│   ├── ai/                # Funcions d'IA
│   └── database/          # Gestió de base de dades
├── config/                # Configuracions
├── docs/                  # Documentació
├── tests/                 # Tests automatitzats
├── assets/                # Recursos estàtics
└── README.md
```

## 🤝 Contribucions

Les contribucions són benvingudes! Obre un issue o envia un pull request.

## 📄 Llicència

MIT License - Consulta [LICENSE](LICENSE) per més detalls.

## 🎯 Objectius d'Aprenentatge

- Desenvolupament de bots
- Integració d'APIs externes
- Intel·ligència artificial aplicada
- Gestió de bases de dades
- Arquitectura de software
- DevOps i desplegament

---

**Fet amb ❤️ per demostrar habilitats tècniques i crear algo útil!**
# Discord Poster Bot - Project Overview

## What You've Got

A fully functional Discord bot that creates professional event posters using Python and Pillow (PIL). The bot responds to slash commands and generates beautiful 1080x1920 posters perfect for promoting events.

## Files Included

### Core Files
- **bot.py** - Main bot code with all functionality
- **requirements.txt** - Python dependencies
- **.env.example** - Template for environment variables
- **setup.sh** - Automated setup script

### Documentation
- **README.md** - Complete documentation and guide
- **QUICKSTART.md** - 5-minute setup guide
- **PROJECT_OVERVIEW.md** - This file

### Testing
- **test_poster.py** - Generate sample posters without Discord
- **sample_poster.png** - Example output

## Key Features

### 1. Slash Commands
- `/create_poster` - Create a custom poster
- `/poster_help` - Display help information

### 2. Customization Options
- **3 Color Themes**: default, vibrant, professional
- **Custom Images**: Include event photos via URL
- **Automatic Layout**: Professional design with proper spacing

### 3. Poster Components
- Title (large, bold)
- Hook/description (engaging subtitle)
- Event image (optional)
- When (date/time)
- Where (location)
- Hosts (organizers)
- Decorative elements (bars, dividers)
- Emoji icons (📅 📍 👥)

## How It Works

1. User types `/create_poster` in Discord
2. Discord shows a form with fields
3. User fills in event details
4. Bot generates poster using Pillow/PIL
5. Bot sends poster as PNG image
6. User can download and share

## Technical Stack

- **Discord.py 2.3.2** - Discord API wrapper
- **Pillow 10.1.0** - Image generation
- **aiohttp 3.9.1** - Async image downloads
- **Python 3.8+** - Core language

## Setup Time

- **Quick setup**: 5 minutes (with token ready)
- **Full setup**: 10-15 minutes (includes Discord app creation)

## Use Cases

- Community events
- Gaming tournaments
- Meetups and gatherings
- Fundraisers
- Workshops and classes
- Parties and celebrations
- Virtual events
- Server announcements

## Customization Ideas

### Easy Modifications
- Add more color themes
- Change poster dimensions
- Modify font sizes
- Adjust spacing and layout

### Advanced Features to Add
- Multiple poster templates
- QR code generation
- User-uploaded fonts
- Image filters/effects
- Multi-page posters
- Calendar integration
- RSVP tracking
- Animated GIF export

## Security Notes

- Bot token must be kept secret
- Use environment variables
- Never commit .env to git
- Regenerate token if exposed

## Performance

- Poster generation: < 2 seconds
- Image download: Depends on source
- Supports multiple concurrent requests
- Low resource usage

## Limitations

- Image must be publicly accessible URL
- Discord file upload limit: 8MB (Nitro: 50MB)
- Slash commands sync delay: 1-2 minutes
- Font customization requires server access

## Getting Help

1. **Common issues**: Check README troubleshooting section
2. **Discord.py docs**: https://discordpy.readthedocs.io/
3. **Pillow docs**: https://pillow.readthedocs.io/
4. **Discord Developer Portal**: https://discord.com/developers/

## Example Usage

```
/create_poster 
  title: Community Game Night
  hook: Join us for board games and fun!
  when: Friday, Dec 1st at 7 PM
  where: Community Center
  hosts: Gaming Club
  theme: vibrant
```

Result: Professional poster in ~2 seconds

## File Structure

```
discord-poster-bot/
├── bot.py                  # Main bot code
├── test_poster.py          # Test script
├── requirements.txt        # Dependencies
├── .env.example           # Token template
├── .env                   # Your token (create this)
├── setup.sh              # Setup automation
├── README.md             # Full documentation
├── QUICKSTART.md         # Quick guide
├── PROJECT_OVERVIEW.md   # This file
└── sample_poster.png     # Example output
```

## Quick Commands Reference

```bash
# Setup
pip install -r requirements.txt
cp .env.example .env
# (edit .env with your token)

# Run
python3 bot.py

# Test
python3 test_poster.py
```

## Next Steps

1. ✅ Files are ready
2. ⏭️ Get Discord bot token
3. ⏭️ Configure .env file
4. ⏭️ Invite bot to server
5. ⏭️ Run and test
6. ⏭️ Customize to your needs

## Support the Project

Ways to improve:
- Add more themes
- Create template library
- Implement caching
- Add analytics
- Create web dashboard
- Support multiple languages

---

**Ready to get started?** 
Open QUICKSTART.md and follow the 6 steps!

**Want full details?** 
Check out README.md for comprehensive documentation.

**Just want to test?** 
Run: `python3 test_poster.py`

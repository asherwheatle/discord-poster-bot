# Discord Poster Bot 🎨

A Discord bot that automatically creates beautiful event posters based on user input. Perfect for promoting events, meetups, and gatherings in your Discord server!

## Features

- **Slash Commands**: Easy-to-use `/create_poster` command
- **Customizable Themes**: Choose from default, vibrant, or professional color schemes
- **Image Support**: Include custom images in your posters
- **Automatic Layout**: Professional poster design with proper text wrapping and spacing
- **High Quality**: Generates 1080x1920 posters perfect for social media

## Prerequisites

- Python 3.8 or higher
- A Discord Bot Token (from [Discord Developer Portal](https://discord.com/developers/applications))
- Discord bot with the following permissions:
  - Send Messages
  - Use Slash Commands
  - Attach Files

## Installation

1. **Clone or download the bot files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Discord Bot**:
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application
   - Go to the "Bot" section and create a bot
   - Copy the bot token
   - Enable "Message Content Intent" under Privileged Gateway Intents

4. **Configure the bot**:
   - Copy `.env.example` to `.env`
   - Add your bot token:
     ```
     DISCORD_BOT_TOKEN=your_actual_token_here
     ```

5. **Invite the bot to your server**:
   - Go to OAuth2 → URL Generator in the Developer Portal
   - Select scopes: `bot`, `applications.commands`
   - Select permissions: `Send Messages`, `Attach Files`, `Use Slash Commands`
   - Use the generated URL to invite the bot

## Usage

### Starting the Bot

```bash
python bot.py
```

Or with environment variable directly:
```bash
export DISCORD_BOT_TOKEN='your_token_here'
python bot.py
```

### Creating a Poster

Use the `/create_poster` slash command with the following parameters:

**Required:**
- `title`: Event title
- `hook`: Catchy hook or description
- `when`: Date and time of the event
- `where`: Location of the event
- `hosts`: Host name(s)

**Optional:**
- `image_url`: URL of an image to include in the poster
- `theme`: Color scheme (`default`, `vibrant`, or `professional`)

### Example Commands

**Basic poster:**
```
/create_poster 
  title: Summer Pool Party
  hook: Join us for an afternoon of fun in the sun!
  when: Saturday, July 15th at 2 PM
  where: Community Pool, 123 Main St
  hosts: The Recreation Committee
```

**With image and theme:**
```
/create_poster 
  title: Gaming Tournament
  hook: Compete for the championship title!
  when: Friday, August 4th at 6 PM
  where: Discord Voice Channels
  hosts: Game Masters Guild
  image_url: https://example.com/gaming-image.jpg
  theme: vibrant
```

**Professional event:**
```
/create_poster 
  title: Annual Fundraiser Gala
  hook: Supporting our community, one event at a time
  when: October 20th, 2024 at 7:00 PM
  where: Grand Ballroom, City Center
  hosts: Sarah Johnson & Michael Chen
  theme: professional
```

### Getting Help

Use `/poster_help` to display information about the bot and available commands.

## Themes

### Default Theme
- Blue and purple tones
- Modern and versatile
- Great for general events

### Vibrant Theme
- Bright pink and cyan colors
- Eye-catching and energetic
- Perfect for parties and casual events

### Professional Theme
- Clean and minimal design
- Soft colors with dark text
- Ideal for formal events and business gatherings

## Poster Specifications

- **Size**: 1080 x 1920 pixels (Instagram/Story format)
- **Format**: PNG with high quality
- **Features**:
  - Automatic text wrapping
  - Image integration with shadows
  - Decorative elements
  - Emoji icons for sections
  - Professional typography

## Troubleshooting

### Bot doesn't respond
- Make sure the bot is online and connected
- Verify slash commands are synced (check console output)
- Ensure the bot has proper permissions

### Image not loading
- Verify the image URL is publicly accessible
- Check that the URL points directly to an image file
- Ensure the image format is supported (JPG, PNG, etc.)

### Commands not showing
- Wait a few minutes for Discord to sync commands
- Try kicking and re-inviting the bot
- Restart the bot

### Font issues
- The bot uses DejaVu Sans fonts (pre-installed on most systems)
- If fonts aren't available, it falls back to default fonts

## Customization

You can customize the bot by modifying `bot.py`:

- **Poster dimensions**: Change `self.width` and `self.height` in `PosterGenerator.__init__`
- **Color schemes**: Add new themes to `self.colors` dictionary
- **Fonts**: Modify font paths and sizes in `create_poster` method
- **Layout**: Adjust spacing, positioning, and decorative elements

## Technical Details

### Dependencies
- **discord.py**: Discord API wrapper
- **Pillow (PIL)**: Image processing and generation
- **aiohttp**: Async HTTP client for downloading images
- **python-dotenv**: Environment variable management

### Architecture
- **Bot class**: Handles Discord connection and events
- **PosterGenerator class**: Creates poster images with PIL
- **Slash commands**: Modern Discord interaction system
- **Async design**: Non-blocking image generation and downloads

## Tips for Best Results

1. **Keep titles short**: 3-6 words work best
2. **Hook should be compelling**: 10-20 words is ideal
3. **Use high-quality images**: At least 800x600 pixels
4. **Match theme to event**: Vibrant for parties, professional for formal events
5. **Include all relevant details**: Date, time, location, and hosts

## Security Notes

- Never commit your `.env` file or bot token to version control
- Keep your bot token private and secure
- Regenerate token if it's ever exposed
- Use environment variables for sensitive data

## License

This bot is provided as-is for educational and personal use.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review Discord.py documentation
3. Verify bot permissions and intents

## Future Enhancements

Possible improvements:
- Additional themes and templates
- Custom font uploads
- Multiple poster size options
- QR code generation
- Export to different formats
- Poster templates library
- Interactive poster editor

---

Made with ❤️ for the Discord community

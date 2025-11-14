# Troubleshooting Guide 🔧

Common issues and their solutions for the Discord Poster Bot.

## Installation Issues

### "pip: command not found"
**Solution:**
- Install pip: `sudo apt-get install python3-pip` (Linux)
- Or use: `python3 -m pip install -r requirements.txt`

### "Permission denied" when installing packages
**Solution:**
```bash
pip install --user -r requirements.txt
```
Or use a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### "ModuleNotFoundError: No module named 'discord'"
**Solution:**
```bash
pip install discord.py
```
Or reinstall all dependencies:
```bash
pip install -r requirements.txt
```

## Bot Connection Issues

### "Invalid token" or "Improper token has been passed"
**Causes & Solutions:**

1. **Wrong token**
   - Go to Discord Developer Portal
   - Click "Reset Token" and copy the new one
   - Update your .env file

2. **Extra spaces in token**
   - Open .env file
   - Make sure there are no spaces around the token
   - Should be: `DISCORD_BOT_TOKEN=your_token_here`

3. **Token not loaded**
   - Make sure .env file is in the same directory as bot.py
   - Or use: `export DISCORD_BOT_TOKEN='your_token'`

### Bot connects but doesn't respond
**Solution:**
1. Check if slash commands are synced:
   - Look for "Synced X command(s)" in console
   - Wait 1-2 minutes for Discord to update

2. Verify bot permissions:
   - Bot needs "Use Slash Commands" permission
   - Reinvite bot with correct permissions

3. Check bot's role position:
   - Bot's role must be high enough in server hierarchy

## Slash Command Issues

### Commands not showing up in Discord
**Solutions:**

1. **Wait for sync**
   - Discord takes 1-2 minutes to update commands
   - Restart bot after waiting

2. **Manual sync**
   - Remove bot from server
   - Re-invite with proper scopes
   - Wait for commands to appear

3. **Check bot scope**
   - When inviting, select both:
     - `bot`
     - `applications.commands`

### "Application did not respond"
**Solutions:**

1. **Check bot is running**
   - Make sure bot.py is still running
   - Look for error messages in console

2. **Increase timeout**
   - This usually means the bot crashed
   - Check error logs
   - Restart the bot

3. **Defer response**
   - Already implemented in code with `interaction.response.defer()`
   - If still happening, check for other errors

## Image Issues

### Images not loading in poster
**Causes & Solutions:**

1. **URL not accessible**
   - Test URL in browser
   - Make sure it's a direct image link
   - Should end in .jpg, .png, .gif, etc.

2. **HTTPS required**
   - Discord requires HTTPS URLs
   - HTTP links won't work

3. **Image too large**
   - Large images may timeout
   - Try a smaller image
   - Recommended: < 5MB

### "Error downloading image"
**Solutions:**
- Verify URL is correct
- Check internet connection
- Try a different image host
- Some sites block bot requests

### Poster looks wrong with custom image
**Solutions:**
- Use landscape or square images for best results
- Minimum recommended size: 800x600
- Very tall images may look stretched

## Font Issues

### Fonts look wrong or generic
**Cause:** DejaVu fonts not installed

**Linux:**
```bash
sudo apt-get install fonts-dejavu
```

**Mac:**
Fonts usually pre-installed

**Windows:**
Download from: https://dejavu-fonts.github.io/

### Want to use custom fonts
**Solution:**
1. Download .ttf font file
2. Place in project directory
3. Edit bot.py, line ~82:
```python
title_font = ImageFont.truetype("your_font.ttf", 90)
```

## Runtime Errors

### "Cannot open image" or PIL errors
**Solutions:**
1. Reinstall Pillow:
```bash
pip uninstall Pillow
pip install Pillow
```

2. Check image format:
```bash
python3 -c "from PIL import Image; print(Image.OPEN)"
```

### "aiohttp error" or network issues
**Solutions:**
1. Check internet connection
2. Verify firewall settings
3. Update aiohttp:
```bash
pip install --upgrade aiohttp
```

### Bot crashes when creating poster
**Debug steps:**
1. Check console for error message
2. Run test script to isolate issue:
```bash
python3 test_poster.py
```
3. If test works but bot doesn't, issue is with Discord connection

## Performance Issues

### Poster generation is slow
**Causes:**
- Large image download
- Slow internet connection
- Server overload

**Solutions:**
- Use smaller images
- Compress images before uploading
- Consider caching popular images

### Bot times out
**Solutions:**
- Increase `max_tokens` (not applicable here)
- Optimize image processing
- Use smaller images
- Check server resources

## Permission Issues

### "Missing Permissions" error
**Solution:**
Ensure bot has these permissions:
- ✅ Send Messages
- ✅ Attach Files
- ✅ Embed Links
- ✅ Use Slash Commands

Reinvite bot with correct permissions.

### Can't use commands in certain channels
**Solution:**
- Check channel permissions for bot role
- Make sure bot can "Use Slash Commands" in that channel
- Check server settings

## Theme Issues

### Theme parameter doesn't work
**Solution:**
- Valid themes: `default`, `vibrant`, `professional`
- Check spelling (case-sensitive)
- If invalid, bot uses default theme

### Want to create custom theme
**Solution:**
Edit bot.py, line ~30, add your theme:
```python
'mytheme': {
    'background': (R, G, B),
    'primary': (R, G, B),
    'secondary': (R, G, B),
    'text': (R, G, B),
    'accent': (R, G, B)
}
```

## Testing Issues

### test_poster.py fails
**Solutions:**
1. Check Pillow installation:
```bash
pip install Pillow
```

2. Verify font paths:
```bash
ls /usr/share/fonts/truetype/dejavu/
```

3. Run with verbose errors:
```bash
python3 -u test_poster.py
```

## Discord Developer Portal Issues

### Can't create bot
**Solution:**
- Log into Discord in browser
- Go to https://discord.com/developers/applications
- You need an account in good standing

### Can't reset token
**Solution:**
- You may have hit rate limit
- Wait 15 minutes and try again
- Check if 2FA is required

## General Debugging

### Enable debug logging
Add to bot.py after imports:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check Python version
```bash
python3 --version
```
Need Python 3.8+

### Verify all dependencies
```bash
pip list | grep -E "discord|Pillow|aiohttp"
```

### Test Discord connection
```python
python3 -c "import discord; print(discord.__version__)"
```

## Still Having Issues?

1. **Check the logs**
   - Look at console output
   - Note exact error messages

2. **Isolate the problem**
   - Does test_poster.py work?
   - Is bot connecting to Discord?
   - Are commands appearing?

3. **Verify setup**
   - Review QUICKSTART.md
   - Double-check each step
   - Ensure all files are present

4. **Common fix: Start fresh**
   ```bash
   # Deactivate any virtual env
   deactivate
   
   # Reinstall dependencies
   pip uninstall discord.py Pillow aiohttp
   pip install -r requirements.txt
   
   # Reset bot token
   # (In Discord Developer Portal)
   
   # Update .env file
   # Run bot
   python3 bot.py
   ```

## Error Message Reference

| Error | Meaning | Solution |
|-------|---------|----------|
| "Invalid token" | Bot token wrong/expired | Reset token in portal |
| "Missing permissions" | Bot lacks permissions | Check permissions |
| "Application did not respond" | Bot crashed/slow | Check logs, restart |
| "Module not found" | Missing package | Install requirements |
| "Cannot connect" | Network/Discord issue | Check connection |
| "Rate limit" | Too many requests | Wait and retry |

## Need More Help?

- Discord.py docs: https://discordpy.readthedocs.io/
- Discord Developer docs: https://discord.com/developers/docs
- Python PIL docs: https://pillow.readthedocs.io/

---

**Pro tip:** Most issues are solved by:
1. Checking bot token is correct
2. Verifying bot permissions
3. Waiting for command sync
4. Restarting the bot

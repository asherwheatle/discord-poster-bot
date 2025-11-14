# Quick Start Guide 🚀

Get your Discord Poster Bot running in 5 minutes!

## Step 1: Get Your Bot Token

1. Go to https://discord.com/developers/applications
2. Click "New Application" and give it a name
3. Go to the "Bot" section in the left sidebar
4. Click "Reset Token" and copy your bot token
5. Under "Privileged Gateway Intents", enable:
   - ✅ Message Content Intent

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 3: Configure Your Token

Create a `.env` file in the same folder as bot.py:

```bash
DISCORD_BOT_TOKEN=paste_your_token_here
```

Or set it as an environment variable:

```bash
export DISCORD_BOT_TOKEN='paste_your_token_here'
```

## Step 4: Invite Bot to Your Server

1. In Discord Developer Portal, go to OAuth2 → URL Generator
2. Select these scopes:
   - ✅ bot
   - ✅ applications.commands
3. Select these bot permissions:
   - ✅ Send Messages
   - ✅ Attach Files
   - ✅ Use Slash Commands
4. Copy the generated URL and open it in your browser
5. Select your server and authorize

## Step 5: Run the Bot

```bash
python bot.py
```

You should see:
```
your_bot_name has connected to Discord!
Synced X command(s)
```

## Step 6: Create Your First Poster!

In any channel where the bot has access, type:

```
/create_poster
```

Then fill in:
- **title**: "Test Event"
- **hook**: "This is my first poster!"
- **when**: "Today at 5 PM"
- **where**: "Discord Server"
- **hosts**: "Me"

Press Enter and watch the magic happen! 🎨

## Common Issues

### "Commands not showing up"
- Wait 1-2 minutes for Discord to sync
- Restart the bot
- Check bot permissions

### "Module not found"
```bash
pip install -r requirements.txt
```

### "Invalid token"
- Double-check your token in Discord Developer Portal
- Make sure there are no extra spaces
- Try resetting the token

## Next Steps

- Try different themes: `default`, `vibrant`, `professional`
- Add images with the `image_url` parameter
- Read the full README.md for advanced usage

---

Need help? Check the full README.md file!

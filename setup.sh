#!/bin/bash
# Discord Poster Bot Setup Script

echo "🎨 Discord Poster Bot Setup"
echo "============================"
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✅ Found Python $PYTHON_VERSION"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt
if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi
echo ""

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  No .env file found"
    echo ""
    echo "Please create a .env file with your Discord bot token:"
    echo "1. Copy .env.example to .env"
    echo "2. Add your bot token from https://discord.com/developers/applications"
    echo ""
    echo "Run: cp .env.example .env"
    echo "Then edit .env and add your token"
    echo ""
else
    echo "✅ Found .env file"
    echo ""
fi

# Create sample poster
echo "🎨 Generating sample poster..."
python3 test_poster.py
if [ $? -eq 0 ]; then
    echo "✅ Sample poster created: sample_poster.png"
else
    echo "⚠️  Could not create sample poster (non-critical)"
fi
echo ""

echo "============================"
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Configure your bot token in .env"
echo "2. Invite the bot to your server"
echo "3. Run: python3 bot.py"
echo ""
echo "📖 Read QUICKSTART.md for detailed instructions"
echo "📚 Read README.md for full documentation"
echo ""

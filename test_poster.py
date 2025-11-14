#!/usr/bin/env python3
"""
Test script to generate a sample poster without Discord
"""

from PIL import Image, ImageDraw, ImageFont
import io

def create_sample_poster():
    """Generate a sample poster to demonstrate the bot's capabilities"""
    
    width = 1080
    height = 1920
    
    # Default theme colors
    colors = {
        'background': (30, 30, 50),
        'primary': (100, 150, 255),
        'secondary': (255, 200, 100),
        'text': (255, 255, 255),
        'accent': (200, 100, 255)
    }
    
    # Create base image
    img = Image.new('RGB', (width, height), colors['background'])
    draw = ImageDraw.Draw(img)
    
    # Load fonts
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 90)
        hook_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 45)
        detail_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
        label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 35)
    except:
        title_font = ImageFont.load_default()
        hook_font = ImageFont.load_default()
        detail_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
    
    y_position = 80
    padding = 60
    
    # Add decorative top bar
    draw.rectangle([0, 0, width, 30], fill=colors['primary'])
    
    # Sample data
    title = "SUMMER POOL PARTY"
    hook = "Join us for an afternoon of fun in the sun!"
    when = "Saturday, July 15th at 2 PM"
    where = "Community Pool, 123 Main St"
    hosts = "The Recreation Committee"
    
    # Draw title
    def get_wrapped_text(text, font, max_width):
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            bbox = font.getbbox(test_line)
            width_text = bbox[2] - bbox[0]
            
            if width_text <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines
    
    # Add placeholder for image
    y_position = 80
    img_height = 500
    draw.rectangle([padding, y_position, width - padding, y_position + img_height], 
                  fill=colors['primary'], outline=colors['secondary'], width=5)
    
    # Draw "IMAGE AREA" text
    placeholder_text = "[Event Image]"
    bbox = hook_font.getbbox(placeholder_text)
    text_width = bbox[2] - bbox[0]
    draw.text(((width - text_width) // 2, y_position + img_height // 2 - 20), 
             placeholder_text, fill=colors['text'], font=hook_font)
    
    y_position += img_height + 80
    
    # Draw title
    title_lines = get_wrapped_text(title, title_font, width - 2 * padding)
    for line in title_lines:
        bbox = title_font.getbbox(line)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (width - text_width) // 2
        
        # Add text shadow
        draw.text((x + 3, y_position + 3), line, fill=(0, 0, 0, 128), font=title_font)
        draw.text((x, y_position), line, fill=colors['primary'], font=title_font)
        y_position += text_height + 20
    
    y_position += 40
    
    # Draw hook
    hook_lines = get_wrapped_text(hook, hook_font, width - 2 * padding)
    for line in hook_lines:
        bbox = hook_font.getbbox(line)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (width - text_width) // 2
        draw.text((x, y_position), line, fill=colors['text'], font=hook_font)
        y_position += text_height + 15
    
    y_position += 60
    
    # Add decorative divider
    divider_y = y_position
    draw.rectangle([padding, divider_y, width - padding, divider_y + 4], 
                  fill=colors['secondary'])
    y_position += 60
    
    # Draw details section
    details = [
        ("📅 WHEN", when),
        ("📍 WHERE", where),
        ("👥 HOSTED BY", hosts)
    ]
    
    for label, value in details:
        # Draw label
        draw.text((padding, y_position), label, fill=colors['secondary'], font=label_font)
        bbox = label_font.getbbox(label)
        y_position += bbox[3] - bbox[1] + 20
        
        # Draw value
        value_lines = get_wrapped_text(value, detail_font, width - 2 * padding)
        for line in value_lines:
            draw.text((padding, y_position), line, fill=colors['text'], font=detail_font)
            bbox = detail_font.getbbox(line)
            y_position += bbox[3] - bbox[1] + 15
        
        y_position += 40
    
    # Add decorative bottom bar
    draw.rectangle([0, height - 30, width, height], fill=colors['accent'])
    
    # Save the image
    img.save('/home/claude/sample_poster.png', quality=95)
    print("✅ Sample poster created: sample_poster.png")
    print(f"   Dimensions: {width}x{height} pixels")

if __name__ == "__main__":
    create_sample_poster()

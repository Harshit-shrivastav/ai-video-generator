import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import numpy as np

def generate_background_image(width, height, background_color, border_width, border_color):
    image = Image.new('RGBA', (width, height), background_color + (255,))
    border_top_bottom = Image.new('RGBA', (width, border_width), border_color + (255,))
    border_left_right = Image.new('RGBA', (border_width, height), border_color + (255,))

    image.paste(border_top_bottom, (0, 0))
    image.paste(border_top_bottom, (0, height - border_width))
    image.paste(border_left_right, (0, 0))
    image.paste(border_left_right, (width - border_width, 0))

    return image

def load_font(font_path, font_size):
    if font_path.startswith("http://") or font_path.startswith("https://"):
        response = requests.get(font_path)
        font = ImageFont.truetype(BytesIO(response.content), font_size)
    else:
        font = ImageFont.truetype(font_path, font_size)
    return font

def write_text_on_image(background_image, text, font_path="https://github.com/Harshit-shrivastav/ai-video-generator/raw/v2/assets/fonts/RobotoCondensed-Black.ttf", font_size=100, text_color=(0, 0, 0)):
    width, height = background_image.size
    draw = ImageDraw.Draw(background_image)
    font = load_font(font_path, font_size)
    text_x = 100
    text_y = 100
    line_width = 0
    max_height = height - 100 - font_size
    words = text.split()
    remaining_text = []
    written_text = []
    last_period_index = None

    for i, word in enumerate(words):
        word_width = font.getlength(word)

        # Handle long words that don't fit on a single line
        if word_width >= width - 200:
            for char in word:
                char_width = font.getlength(char)
                if line_width + char_width >= width - 200:
                    text_y += font_size
                    if text_y >= max_height:
                        remaining_text = words[i:]
                        break
                    line_width = char_width
                else:
                    line_width += char_width
                written_text.append(char)
                draw.text((text_x + line_width - char_width, text_y), char, font=font, fill=text_color)
            continue

        if word.endswith('.'):
            last_period_index = i + 1

        if line_width + word_width >= width - 200:
            text_y += font_size
            if text_y >= max_height:
                remaining_text = words[i:]
                break
            line_width = word_width
        else:
            line_width += word_width + font.getlength(' ')
        written_text.append(word)
        draw.text((text_x + line_width - word_width, text_y), word, font=font, fill=text_color)

    if last_period_index is not None:
        written_text = written_text[:last_period_index]
        remaining_text = words[last_period_index:]

    written_text_str = ' '.join(written_text)
    if remaining_text:
        extra_text = ' '.join(remaining_text)
    else:
        extra_text = None

    return background_image, extra_text, written_text_str

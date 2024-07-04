from PIL import Image, ImageDraw, ImageFont
import textwrap
import base64
import os
import yaml
import json
from io import BytesIO

def load_config(config_file):
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    return config

def load_font(font_path, font_size):
    try:
        font = ImageFont.truetype(font_path, size=font_size)
    except IOError:
        font = ImageFont.load_default()
    return font

def wrap_text(text, wrap_width):
    lines = []
    for line in text.splitlines():
        lines.extend(textwrap.wrap(line, width=wrap_width))
    return lines

def calculate_total_height(lines, font):
    line_heights = [font.getsize(line)[1] for line in lines]
    total_height = sum(line_heights)
    return total_height

def create_image(width, height, color='white'):
    return Image.new('RGB', (width, height), color=color)

def draw_text_on_image(image, lines, font, margin=10):
    draw = ImageDraw.Draw(image)
    y = margin
    for line in lines:
        draw.text((margin, y), line, font=font, fill='black')
        y += font.getsize(line)[1]  # Move y coordinate down by the height of the current line

def save_image(image, output_filename):
    script_dir = os.path.dirname(__file__)
    image_path = os.path.join(script_dir, output_filename)
    image.save(image_path, format='PNG')
    return image_path

def encode_image_base64(image):
    image_stream = BytesIO()
    image.save(image_stream, format='PNG')
    image_stream.seek(0)
    image_base64 = base64.b64encode(image_stream.read()).decode('utf-8')
    image_url = f"data:image/png;base64,{image_base64}"
    return image_url

def generate_images(input_data, config):
    # Load font and other parameters from config
    font = load_font(config['font_path'], config['font_size'])
    output_width = config['output_width']
    output_height = config['output_height']
    wrap_width = output_width // config['wrap_factor']
    
    generated_images = {}
    
    for key, text in input_data.items():
        # Wrap text
        lines = wrap_text(text, wrap_width)
        
        # Calculate total height needed for the text
        total_height = calculate_total_height(lines, font)
        
        # Create a new image with adjusted height
        image = create_image(output_width, max(total_height + 20, output_height))
        
        # Draw text on the image
        draw_text_on_image(image, lines, font)
        
        # Save the image
        output_filename = f"{key}.png"  # Use key as part of filename
        image_path = save_image(image, output_filename)
        
        # Encode image to base64
        image_url = encode_image_base64(image)
        
        # Generate HTML img tag
        img_tag = f'<img src="{image_url}" alt="{key}">'
        
        # Store img tag in generated_images dictionary
        generated_images[key] = img_tag
    
    # Write HTML img tags to JSON file
    output_json_file = config.get('output_json_file', 'output_html_tags.json')
    with open(output_json_file, 'w') as f:
        json.dump(generated_images, f, indent=2)
    
    return generated_images

if __name__ == "__main__":
    # Read config file
    config = load_config('config.yaml')
    
    # Read input data from input.yaml
    with open('input.yaml', 'r') as f:
        input_data = yaml.safe_load(f)
    
    # Generate images
    generated_images = generate_images(input_data, config)
    
    # for key, img_tag in generated_images.items():
    #     # print(f"\nHTML img tag for '{key}':")
    #     # print(img_tag)
    
    # Inform user about the output JSON file
    output_json_file = config.get('output_json_file', 'output_html_tags.json')
    print(f"\nHTML img tags written to: {output_json_file}")

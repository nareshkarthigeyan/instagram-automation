import os
import random
import textwrap
import requests
from PIL import Image, ImageDraw, ImageFont
from instagrapi import Client
from dotenv import load_dotenv
import json
from datetime import datetime
import time

# Load environment variables from .env file
load_dotenv()

script_path = "/home/nareshkarthigeyan/Naresh/cs/code/intagramautomater-python/"

def create_image_with_text(text, image_counter_path=script_path + "image_counter.txt"):
    try:
        # Read and increment the image counter
        if os.path.exists(image_counter_path):
            with open(image_counter_path, "r") as f:
                count = int(f.read().strip())
        else:
            count = 0
        count += 1
        with open(image_counter_path, "w") as f:
            f.write(str(count))
        
        # Create a new image with black background
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        image = Image.new("RGBA", (1200, 1200), (r, g, b, 255))
        draw = ImageDraw.Draw(image)

        # Load a font
        fontList = ["FreeMonoBoldOblique.ttf", "FreeMono.ttf","FreeSansOblique.ttf","FreeSerifBold.ttf",'FreeMonoBold.ttf','FreeSansBoldOblique.ttf','FreeSans.ttf','FreeSerifItalic.ttf','FreeMonoOblique.ttf','FreeSansBold.ttf','FreeSerifBoldItalic.ttf','FreeSerif.ttf']
        fontChosen = random.choice(fontList)
        font_path = f"/usr/share/fonts/truetype/freefont/{fontChosen}" 
        if not os.path.exists(font_path):
            raise FileNotFoundError(f"Font file not found: {font_path}")
        if len(text) > 25:
            size = random.randint(28, 72)
        else:
            size = random.randint(32, 92)
        font = ImageFont.truetype(font_path, size)

        text_width, text_height = 800, 800  # Maximum width and height of the text box
        # Add text to image
        rightLimit = 200
        x = random.randint(8, 120)
        y = random.randint(8, 111)
        # wrapped_text = textwrap.fill(text, width=50) 
        # brightness = 1
        # draw.text((x, y), wrapped_text, font=font, fill=((255 - r)*brightness, (255 - g)*brightness, (255- b)*brightness, 255))

        margin = offset = 40
        for line in textwrap.wrap(text, width=40):
            draw.text((margin, offset), line, font=font, fill=((255 - r), (255 - g), (255- b), 255))
            offset += font.getbbox(line)[3] + 10

        # Save the image
        image_path = script_path + f"posts/{count}.png"
        os.makedirs(os.path.dirname(image_path), exist_ok=True)
        image.save(image_path)
        print(f"Image with text created: {image_path}")
        return image_path
    except Exception as e:
        print(f"Error creating image: {e}")
        raise

def post_to_insta(text, caption):
    try:
        # Create an image with the provided text
        print("Locating File")
        image_path = create_image_with_text(text)

        # Initialize the Instagram client
        print("Logging In...")
        ig = Client()
        ig.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))

        # Post the image to Instagram
        print("Uploading...")
        ig.photo_upload(image_path, caption)
        print("Post Successful.")
        return 1
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1

def main():
    content_path = script_path + "content.json"
    with open(content_path, "r") as f:
        data = json.load(f)
        quotes = data["quotes"]  # Assuming "quotes" is the key for the list of quotes
    
    chosen = random.randint(0, len(quotes) - 1)
    print(chosen)
    chosen_quote = quotes[chosen]
    text = chosen_quote["quote"]
    print(text)
    caption = ""  # You can add caption logic here if needed
    x = post_to_insta(text, caption)
    if x == 0:
        quotes.pop(chosen)
        with open(content_path, "w") as f:
            json.dump({"quotes": quotes}, f, indent=4) 


if __name__ == "__main__":
    main()

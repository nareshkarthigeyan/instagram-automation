import numpy as np
import matplotlib.pyplot as plt
import os
import random
import requests
import textwrap
from PIL import Image, ImageDraw, ImageFont
from instagrapi import Client
from dotenv import load_dotenv
import json
import datetime
import time

load_dotenv()

script_path = "/home/nareshkarthigeyan/Naresh/cs/code/intagramautomater-python/"

def getPostCount(image_counter_path=script_path + "image_counter.txt"):
    if os.path.exists(image_counter_path):
        with open(image_counter_path, "r") as f:
            count = int(f.read().strip())
    else:
        count = 0
    count += 1
    with open(image_counter_path, "w") as f:
        f.write(str(count))
    return count

def create_image_with_text(text, image_counter_path=script_path + "image_counter.txt"):
    try:
        count = getPostCount()

        r = 0
        g = 0
        b = 0
        image = Image.new("RGBA", (1200, 1200), (0, 0, 0, 255))
        draw = ImageDraw.Draw(image)

        fontList = [f for f in os.listdir(f"/home/nareshkarthigeyan/Naresh/cs/code/intagramautomater-python/fonts")]
        fontChosen = random.choice(fontList)
        font_path = f"/home/nareshkarthigeyan/Naresh/cs/code/intagramautomater-python/fonts/{fontChosen}" 
        if not os.path.exists(font_path):
            raise FileNotFoundError(f"Font file not found: {font_path}")
        # if len(text) > 24:
        #     size = random.randint(32, 72)
        # else:
        #     size = random.randint(36, 82)
        size = 42
        font = ImageFont.truetype(font_path, size)

        text_width, text_height = 800, 800  

        x = 50
        y = 50

        if size > 59:
            text_width = 25
        else:
            text_width = 38
        for line in textwrap.wrap(text, width=text_width):
            # draw.text((x, y), line, font=font, fill=(255, 255, 255, 255))
            draw.text((x, y), line, font=font, fill=((255 - r), (255 - g), (255- b), 255))
            y += font.getbbox(line)[3] + 10

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
        print("Locating File")
        image_path = create_image_with_text(text)

        time.sleep(7)
        print("Logging In...")
        ig = Client()
        ig.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))

        print("Uploading...")
        ig.photo_upload(image_path, caption)
        print("Post Successful.")
        t = time.localtime()
        print(time.strftime(r"%d/%m/%Y %H:%M:%S.%MS", t))
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1
    


def main():
    content_path = script_path + "content.json"
    with open(content_path, "r") as f:
        data = json.load(f)
        quotes = data["quotes"]
        chosen = getPostCount()
        print(chosen)
        chosen_quote = quotes[chosen]
        text = chosen_quote["quote"]
        print(text)
        caption = f"Day {chosen}"  
        x = post_to_insta(text, caption)
        if x == 0:
            quotes.pop(chosen)
            with open(content_path, "w") as f:
                json.dump({"quotes": quotes}, f, indent=4)


if __name__ == "__main__":
   main()

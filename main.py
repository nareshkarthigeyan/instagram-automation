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

class color:
    def __init__(self):
        self.br = None
        self.bg = None
        self.bb = None
        self.tr = None
        self.tg = None
        self.tb = None

    def getBackgroundColor(self):
        templateBg = [
        # Format: [R, G, B]
        [255, 0, 0],     # Red
        [0, 255, 0],     # Green
        [0, 0, 255],     # Blue
        [255, 255, 0],   # Yellow
        [0, 255, 255],   # Cyan
        [255, 0, 255],   # Magenta
        [128, 0, 0],     # Maroon
        [128, 128, 0],   # Olive
        [0, 128, 0],     # Dark Green
        [128, 0, 128],   # Purple
        [0, 128, 128],   # Teal
        [0, 0, 128],     # Navy
        [255, 165, 0],   # Orange
        [75, 0, 130],    # Indigo
        [240, 248, 255], # Alice Blue
        [245, 245, 220], # Beige
        [255, 228, 196], # Bisque
        [0, 0, 139],     # Dark Blue
        [255, 255, 240], # Ivory
        [255, 69, 0],    # Orange Red
        [238, 232, 170], # Pale Goldenrod
        [152, 251, 152], # Pale Green
        [219, 112, 147], # Pale Violet Red
        [112, 128, 144], # Slate Gray
        [255, 245, 238], # Seashell
        [244, 164, 96],  # Sandy Brown
        [255, 218, 185], # Peach Puff
        [64, 224, 208],  # Turquoise
        [238, 130, 238], # Violet
        [245, 222, 179], # Wheat
        [0, 255, 127],   # Spring Green
        [127, 255, 212], # Aquamarine
        [210, 105, 30],  # Chocolate
        [220, 20, 60],   # Crimson
        [139, 69, 19],   # Saddle Brown
        [255, 160, 122], # Light Salmon
        [34, 139, 34],   # Forest Green
        [70, 130, 180],  # Steel Blue
        [255, 228, 225], # Misty Rose
        [245, 255, 250], # Mint Cream
        [139, 0, 0],     # Dark Red
        [255, 20, 147],  # Deep Pink
        [255, 228, 181], # Moccasin
        [255, 240, 245], # Lavender Blush
        [255, 182, 193], # Light Pink
        [255, 192, 203], # Pink
        [255, 105, 180], # Hot Pink
        [255, 160, 122], # Light Salmon
        [255, 127, 80],  # Coral
        [250, 128, 114], # Salmon
        [233, 150, 122], # Dark Salmon
        [240, 128, 128], # Light Coral
        [255, 99, 71],   # Tomato
        [255, 69, 0],    # Orange Red
        [255, 140, 0],   # Dark Orange
        [255, 165, 0],   # Orange
        [255, 215, 0],   # Gold
        [238, 232, 170], # Pale Goldenrod
        [240, 230, 140], # Khaki
        [255, 239, 213], # Papaya Whip
        [255, 235, 205], # Blanched Almond
        [255, 222, 173], # Navajo White
        [245, 222, 179], # Wheat
        [255, 248, 220], # Cornsilk
        [255, 250, 205], # Lemon Chiffon
        [250, 250, 210], # Light Goldenrod Yellow
        [255, 255, 224], # Light Yellow
        [255, 255, 240], # Ivory
        [240, 255, 240], # Honeydew
        [240, 255, 255], # Azure
        [240, 248, 255], # Alice Blue
        [248, 248, 255], # Ghost White
        [245, 245, 245], # White Smoke
        [255, 255, 255], # White
        [0, 0, 0],       # Black
        [47, 79, 79],    # Dark Slate Gray
        [105, 105, 105], # Dim Gray
        [169, 169, 169], # Dark Gray
        [192, 192, 192], # Silver
        [211, 211, 211], # Light Gray
        [220, 220, 220], # Gainsboro
        [245, 245, 245], # White Smoke
        [255, 250, 250], # Snow
        [47, 79, 79],    # Dark Slate Gray
        [0, 0, 139],     # Dark Blue
        [0, 0, 205],     # Medium Blue
        [0, 191, 255],   # Deep Sky Blue
        [30, 144, 255],  # Dodger Blue
        [100, 149, 237], # Cornflower Blue
        [135, 206, 235], # Sky Blue
        [173, 216, 230], # Light Blue
        [135, 206, 250], # Light Sky Blue
        ]

        templateTx = [
            # Complementary Colors (Text Colors)
            [0, 255, 255],   # Cyan
            [255, 0, 255],   # Magenta
            [255, 255, 0],   # Yellow
            [0, 0, 255],     # Blue
            [255, 0, 255],   # Magenta
            [0, 255, 0],     # Green
            [0, 255, 255],   # Cyan
            [0, 255, 255],   # Cyan
            [255, 0, 255],   # Magenta
            [255, 255, 0],   # Yellow
            [255, 255, 0],   # Yellow
            [255, 255, 0],   # Yellow
            [0, 0, 255],     # Blue
            [255, 165, 0],   # Orange
            [75, 0, 130],    # Indigo
            [105, 105, 105], # Dim Gray
            [112, 128, 144], # Slate Gray
            [255, 255, 240], # Ivory
            [0, 0, 128],     # Navy
            [75, 0, 130],    # Indigo
            [255, 165, 0],   # Orange
            [0, 128, 128],   # Teal
            [0, 128, 0],     # Dark Green
            [255, 255, 255], # White
            [255, 255, 255], # White
            [0, 0, 0],       # Black
            [105, 105, 105], # Dim Gray
            [220, 20, 60],   # Crimson
            [255, 69, 0],    # Orange Red
            [255, 215, 0],   # Gold
            [0, 255, 255],   # Cyan
            [0, 128, 128],   # Teal
            [0, 0, 255],     # Blue
            [135, 206, 250], # Light Sky Blue
            [105, 105, 105], # Dim Gray
            [240, 248, 255], # Alice Blue
            [255, 0, 255],   # Magenta
            [255, 69, 0],    # Orange Red
            [255, 215, 0],   # Gold
            [75, 0, 130],    # Indigo
            [238, 232, 170], # Pale Goldenrod
            [139, 69, 19],   # Saddle Brown
            [255, 255, 255], # White
            [0, 0, 0],       # Black
            [245, 222, 179], # Wheat
            [255, 255, 255], # White
            [112, 128, 144], # Slate Gray
            [245, 255, 250], # Mint Cream
            [255, 215, 0],   # Gold
            [0, 0, 128],     # Navy
            [173, 216, 230], # Light Blue
            [255, 0, 255],   # Magenta
            [238, 232, 170], # Pale Goldenrod
            [0, 0, 139],     # Dark Blue
            [245, 245, 220], # Beige
            [240, 248, 255], # Alice Blue
            [255, 0, 255],   # Magenta
            [0, 128, 128],   # Teal
            [75, 0, 130],    # Indigo
            [255, 215, 0],   # Gold
            [255, 69, 0],    # Orange Red
            [245, 255, 250], # Mint Cream
            [0, 0, 0],       # Black
            [255, 255, 255], # White
            [47, 79, 79],    # Dark Slate Gray
            [105, 105, 105], # Dim Gray
            [169, 169, 169], # Dark Gray
            [192, 192, 192], # Silver
            [211, 211, 211], # Light Gray
            [220, 220, 220], # Gainsboro
            [245, 245, 245], # White Smoke
            [255, 250, 250], # Snow
            [0, 191, 255],   # Deep Sky Blue
            [173, 216, 230], # Light Blue
            [173, 216, 230], # Light Blue
            [0, 0, 0],       # Black
            [0, 0, 0],       # Black
            [0, 0, 0],       # Black
            [0, 0, 0],       # Black
            [0, 0, 0],       # Black
            [0, 0, 0],       # Black
            [0, 0, 0],       # Black
        ]

        n = random.randint(0, len(templateBg) - 1)
        self.br = templateBg[n][0]
        self.bg = templateBg[n][1]
        self.bb = templateBg[n][2]
        self.tr = templateTx[n][0]
        self.tg = templateTx[n][1]
        self.tb = templateTx[n][2]

script_path = "/home/nareshkarthigeyan/Naresh/cs/code/intagramautomater-python/"

def create_image_with_text(text, image_counter_path=script_path + "image_counter.txt"):
    try:
        if os.path.exists(image_counter_path):
            with open(image_counter_path, "r") as f:
                count = int(f.read().strip())
        else:
            count = 0
        count += 1
        with open(image_counter_path, "w") as f:
            f.write(str(count))

        bgClr = color()
        bgClr.getBackgroundColor()
        # r = random.randint(0, 255)
        # g = random.randint(0, 255)
        # b = random.randint(0, 255)
        image = Image.new("RGBA", (1200, 1200), (bgClr.br, bgClr.bg, bgClr.bb, 255))
        draw = ImageDraw.Draw(image)

        fontList = [f for f in os.listdir(f"/home/nareshkarthigeyan/Naresh/cs/code/intagramautomater-python/fonts")]
        fontChosen = random.choice(fontList)
        font_path = f"/home/nareshkarthigeyan/Naresh/cs/code/intagramautomater-python/fonts/{fontChosen}" 
        if not os.path.exists(font_path):
            raise FileNotFoundError(f"Font file not found: {font_path}")
        if len(text) > 24:
            size = random.randint(32, 72)
        else:
            size = random.randint(36, 82)
        font = ImageFont.truetype(font_path, size)

        text_width, text_height = 800, 800  

        x = random.randint(15, 80)
        y = random.randint(8, 460)

        if size > 59:
            text_width = 25
        else:
            text_width = 38
        for line in textwrap.wrap(text, width=text_width):
            draw.text((x, y), line, font=font, fill=((bgClr.tr), (bgClr.tg), (bgClr.tb), 255))
            # draw.text((x, y), line, font=font, fill=((255 - r), (255 - g), (255- b), 255))
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
    

def fetchQuotesFromAPI():
    categories = ["age", "alone", "amazing", "anger", "architecture", "art", "attitude",
    "beauty", "best", "birthday", "business", "car", "change",
    "communication", "computers", "cool", "courage", "dad", "dating",
    "death", "design", "dreams", "education", "environmental", "equality",
    "experience", "failure", "faith", "family", "famous", "fear", "fitness",
    "food", "forgiveness", "freedom", "friendship", "funny", "future",
    "god", "good", "government", "graduation", "great", "happiness",
    "health", "history", "home", "hope", "humor", "imagination",
    "inspirational", "intelligence", "jealousy", "knowledge", "leadership",
    "learning", "legal", "life", "love", "marriage", "medical", "men",
    "mom", "money", "morning", "movies", "success"]

    category = random.choice(categories)
    apiUrl = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(apiUrl, headers={'X-Api-key': os.getenv("API_NINJA_API")})
    responseString =  response.json()
    return responseString


def main():
    content_path = script_path + "content.json"
    with open(content_path, "r") as f:
        data = json.load(f)
        quotes = data["quotes"]
    if len(quotes) in [0, 1]:
        externalQuote = fetchQuotesFromAPI()
        text = externalQuote[0]["quote"]
        caption = externalQuote[0]["author"]
        print(text,"\n", caption)
        x = post_to_insta(text, caption)
    else:
        chosen = random.randint(0, len(quotes) - 1)
        print(chosen)
        chosen_quote = quotes[chosen]
        text = chosen_quote["quote"]
        print(text)
        caption = f"Quote number {chosen}"  
        x = post_to_insta(text, caption)
        if x == 0:
            quotes.pop(chosen)
            with open(content_path, "w") as f:
                json.dump({"quotes": quotes}, f, indent=4)


if __name__ == "__main__":
    main()

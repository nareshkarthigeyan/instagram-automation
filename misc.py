from main import *
import os

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
        
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        r = 0
        b = 0
        g = 0
        image = Image.open(script_path+"template/template.png")
        draw = ImageDraw.Draw(image)

        fontList = [f for f in os.listdir(f"/home/nareshkarthigeyan/Naresh/cs/code/intagramautomater-python/fonts")]
        fontChosen = random.choice(fontList)
        font_path = f"/home/nareshkarthigeyan/Naresh/cs/code/intagramautomater-python/fonts/{fontChosen}" 
        if not os.path.exists(font_path):
            raise FileNotFoundError(f"Font file not found: {font_path}")
        if len(text) > 25:
            size = random.randint(28, 72)
        else:
            size = random.randint(32, 82)

        size = 48
        font = ImageFont.truetype(font_path, size)

        text_width, text_height = 800, 800  

        x = (1200 - text_height) / 2
        y = (1200 - text_width) / 2

        if size > 59:
            text_width = 35
        else:
            text_width = 42
        for line in textwrap.wrap(text, width=text_width):
            draw.text((x, y), line, font=font, fill=((255 - r), (255 - g), (255- b), 255))
            y += font.getbbox(line)[3] + 10

        # Save the image
        image_path = script_path + f"template/{count}.png"
        os.makedirs(os.path.dirname(image_path), exist_ok=True)
        image.save(image_path)
        print(f"Image with text created: {image_path}")
        return image_path
    except Exception as e:
        print(f"Error creating image: {e}")
        raise

create_image_with_text(f"'Sir... if you don't know what is wrong, then how do you know if something is wrong?\n'That's just how things are sometimes,' said Manjunath. 'They are wrong before they are things.'\n- Kanan Gill, Acts of God")
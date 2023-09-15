

import numpy as np
from PIL import Image,ImageDraw
import os
import math
# We can add more of these later...keeping it simple for now!
script_dir = os.path.dirname(os.path.abspath(__file__))
COLOR_CODES = {
"COLOR_1": os.path.join(script_dir, "BobRoss/cloud1.png"),
"COLOR_2": os.path.join(script_dir, "BobRoss/mountain.png"),
"COLOR_3": os.path.join(script_dir, "BobRoss/sun1.png"),
"COLOR_4": os.path.join(script_dir, "BobRoss/sun2.png"),
"COLOR_5": os.path.join(script_dir, "BobRoss/tree1.png"),
"COLOR_6": os.path.join(script_dir, "BobRoss/tree2.png"),
"COLOR_7": os.path.join(script_dir, "BobRoss/tree3.png"),
"COLOR_8": os.path.join(script_dir, "BobRoss/waterfall.png")
}
HORIZONTAL_PIXELS = 1000;
VERTICAL_PIXELS = 1000;


class MarkovBobRoss:

    def __init__(self, transition_matrix):

     self.transition_matrix = transition_matrix
     self.colors = list(transition_matrix.keys())

    def get_next_color(self, current_color):

        return np.random.choice(
        self.colors,
        p=[self.transition_matrix[current_color][next_color] \
        for next_color in self.colors]
    )
    def get_next_pos(self):
        x = np.random.randint(0, HORIZONTAL_PIXELS)
        y = np.random.randint(0, VERTICAL_PIXELS)
        return (x, y)
    def compose_collage (self, current_color = "COLOR_1", num_images = 15, current_pos = (0,0)):
        image_pos = []
        canvas = Image.new("RGB", (HORIZONTAL_PIXELS, VERTICAL_PIXELS), (171,195,197))
        image_pos.append((current_color,current_pos))
        for index in range (num_images-1):
            next_image = self.get_next_color(current_color)
            next_pos = self.get_next_pos()
            current_color= next_image
            current_pos= next_pos
            image_pos.append((current_color,current_pos))
        for image,pos in image_pos:
            image_path = COLOR_CODES[image]
            if image_path:
                image = Image.open(image_path)
                if image.mode != "RGB":
                    image = image.convert("RGB")

                # Define the color to replace black pixels with (as an RGB tuple)
                new_color = (171, 191, 197)  # Replace black with red (adjust as needed)

                # Iterate through pixels and replace black with the new color
                width, height = image.size
                for x in range(width):
                    for y in range(height):
                        r, g, b = image.getpixel((x, y))
                        if r == 0 and g == 0 and b == 0:  # Check if pixel is black
                            image.putpixel((x, y), new_color)
                scale_factor = math.sqrt((HORIZONTAL_PIXELS*VERTICAL_PIXELS)/15)
                image = image.resize((int(scale_factor), int(scale_factor)))
                canvas.paste(image, pos)
            else:
                print(f"Image path not found for {image}")


        return canvas
            
    
   

    

def main():
        Bob_maker = MarkovBobRoss({
            "COLOR_1": {"COLOR_1": 0.3, "COLOR_2": 0.1, "COLOR_3": 0.2,"COLOR_4": 0.05, "COLOR_5": 0.02, "COLOR_6": 0.1,"COLOR_7": 0.08, "COLOR_8": 0.15},
            "COLOR_2": {"COLOR_1": 0.06, "COLOR_2": 0.25, "COLOR_3": 0.04,"COLOR_4": 0.2, "COLOR_5": 0.05, "COLOR_6": 0.15,"COLOR_7": 0.1, "COLOR_8": 0.15},
            "COLOR_3": {"COLOR_1": 0.2, "COLOR_2": 0.1, "COLOR_3": 0.35,"COLOR_4": 0.05, "COLOR_5": 0.15, "COLOR_6": 0.06,"COLOR_7": 0.06, "COLOR_8": 0.03},
            "COLOR_4": {"COLOR_1": 0.09, "COLOR_2": 0.25, "COLOR_3": 0.02,"COLOR_4": 0.3, "COLOR_5": 0.02, "COLOR_6": 0.15,"COLOR_7": 0.07, "COLOR_8": 0.1},
            "COLOR_5": {"COLOR_1": 0.2, "COLOR_2": 0.06, "COLOR_3": 0.15,"COLOR_4": 0.02, "COLOR_5": 0.35, "COLOR_6": 0.05,"COLOR_7": 0.08, "COLOR_8": 0.09},
            "COLOR_6": {"COLOR_1": 0.05, "COLOR_2": 0.1, "COLOR_3": 0.06,"COLOR_4": 0.2, "COLOR_5": 0.09, "COLOR_6": 0.2,"COLOR_7": 0.15, "COLOR_8": 0.15},
            "COLOR_7": {"COLOR_1": 0.04, "COLOR_2": 0.11, "COLOR_3": 0.04,"COLOR_4": 0.1, "COLOR_5": 0.06, "COLOR_6": 0.15,"COLOR_7": 0.3, "COLOR_8": 0.2},
            "COLOR_8": {"COLOR_1": 0.1, "COLOR_2": 0.1, "COLOR_3": 0.1,"COLOR_4": 0.06, "COLOR_5": 0.1, "COLOR_6": 0.2,"COLOR_7": 0.1, "COLOR_8": 0.24},


    })

        new_art = Bob_maker.compose_collage(current_color="COLOR_1", num_images=40, current_pos= (0,0))
        """make the art with current color and length"""
        new_art.show()
       

        
        print("Process completed!")
if __name__ == "__main__":
        main()






import numpy as np
from PIL import Image,ImageDraw
import os
import math
script_dir = os.path.dirname(os.path.abspath(__file__)) 
#these are the paths for the images
COLOR_CODES = {
"COLOR_1": os.path.join(script_dir, "Assets/BobRoss/cloud1.png"),
"COLOR_2": os.path.join(script_dir, "Assets/BobRoss/mountain.png"),
"COLOR_3": os.path.join(script_dir, "Assets/BobRoss/sun1.png"),
"COLOR_4": os.path.join(script_dir, "Assets/BobRoss/sun2.png"),
"COLOR_5": os.path.join(script_dir, "Assets/BobRoss/tree1.png"),
"COLOR_6": os.path.join(script_dir, "Assets/BobRoss/tree2.png"),
"COLOR_7": os.path.join(script_dir, "Assets/BobRoss/tree3.png"),
"COLOR_8": os.path.join(script_dir, "Assets/BobRoss/waterfall.png")
}
#canvas size
HORIZONTAL_PIXELS = 1000;
VERTICAL_PIXELS = 1000;


class MarkovBobRoss:

    def __init__(self, transition_matrix):

     self.transition_matrix = transition_matrix
     self.images = list(transition_matrix.keys())

#gets the next image from a first order markov chain
    def get_next_image(self, current_image):

        return np.random.choice(
        self.images,
        p=[self.transition_matrix[current_image][next_image] \
        for next_image in self.images]
    )
    #gets a random place for the next position
    def get_next_pos(self):
        x = np.random.randint(0, HORIZONTAL_PIXELS)
        y = np.random.randint(0, VERTICAL_PIXELS)
        return (x, y)

        #adds all of the images it chooses and their postions to a canvas and then turns the black (background) into the background color
    def compose_collage (self, current_image = "COLOR_1", num_images = 15, current_pos = (0,0)):
        image_pos = []
        canvas = Image.new("RGB", (HORIZONTAL_PIXELS, VERTICAL_PIXELS), (171,195,197))
        image_pos.append((current_image,current_pos))
        for index in range (num_images-1):
            next_image = self.get_next_image(current_image)
            next_pos = self.get_next_pos()
            current_image= next_image
            current_pos= next_pos
            image_pos.append((current_image,current_pos))
        for image,pos in image_pos:
            image_path = COLOR_CODES[image]
            if image_path:
                image = Image.open(image_path)
                if image.mode != "RGB":
                    image = image.convert("RGB")

                new_color = (171, 191, 197) 

               
                width, height = image.size
                for x in range(width):
                    for y in range(height):
                        r, g, b = image.getpixel((x, y))
                        if r == 0 and g == 0 and b == 0:  
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

        new_art = Bob_maker.compose_collage(current_image="COLOR_1", num_images=25, current_pos= (0,0))
        
        new_art.show()
       

        
        print("Process completed!")
if __name__ == "__main__":
        main()




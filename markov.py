
import numpy as np
from PIL import Image
# We can add more of these later...keeping it simple for now!
IMAGES = {
"COLOR_1": [107, 174, 193],
"COLOR_2": [30,65,69],
"COLOR_3": [11,135,182],
"COLOR_4": [28,46,37],
"COLOR_5": [171,195,197],
"COLOR_6": [62,99,99],
"COLOR_7": [91,133,137],
"COLOR_8": [59,108,127],

}
POSITIONS = {
    "POSITION_1": (0,0),
    "POSITION_2": (0,0),
    "POSITION_3": (0,0),
    "POSITION_4": (0,0),
    "POSITION_5": (0,0),
    "POSITION_6": (0,0),
    "POSITION_7": (0,0),
    "POSITION_8": (0,0),
    "POSITION_9": (0,0),
    "POSITION_10": (0,0),
    "POSITION_11": (0,0),
    "POSITION_12": (0,0),
    "POSITION_13": (0,0),
    "POSITION_14": (0,0),
    "POSITION_15": (0,0)
}

HORIZONTAL_PIXELS = 25;
VERTICAL_PIXELS = 25;

class MarkovBobRoss:

    def __init__(self, transition_matrix):

     self.transition_matrix = transition_matrix
     self.images = list(transition_matrix.keys())

    def get_next_image(self, current_image):

        return np.random.choice(
        self.images,
        p=[self.transition_matrix[current_image][next_image] \
        for next_image in self.images]
    )

    def get_next_position(self, current_position):
        return np.random.choice(list(self.transition_matrix_positions.keys()),
            p=list(self.transition_matrix_positions[current_position].values())
        )
      
        
    


    def compose_collage(self, current_image="COLOR_1", num_images = 15, current_position = (0,0)):
        collage = Image.new("RGB", (HORIZONTAL_PIXELS, VERTICAL_PIXELS))
        for row in range(num_images):
            next_image = self.get_next_image(current_image)
            next_position = self.get_next_position(current_position)
            image = Image.open(next_image)
            collage.paste(image, next_position)


                
        return collage



    def write_drawing(self, artwork):
        """turns  array into painting"""
        bobbyross = Image.fromarray(artwork, 'RGB')
        bobbyross.save('bobbyross.png')
        return bobbyross

    transition_matrix_positions = {}
    def make_postition_t_matrix(self, current_position):
        next_positions = []
        movements = [
        (-1, 0, 0.1),  # up
        (1, 0, 0.1),   # down
        (0, -1, 0.1),  #left
        (0, 1, 0.2), # right
        (-2, 0, 0.1), #up option 2
        (-2, 0, 0.2), # down option 2
        (0, -2, 0.1), # left option 2
        (0, 2, 0.1) # right option 2
        ]
        for x_transition, y_transition, probability in movements:
            x , y = current_position
            newx = x+x_transition
            newy = y+y_transition
            if 0 <= newx < HORIZONTAL_PIXELS and 0 <= newy < VERTICAL_PIXELS:
             next_positions[(newx, newy)] = probability
            

        #here you need to make sure the probabilites add up to 1
        #and then if not you need to get the difference and scale it to all of the probs at the moment
        #then return next_prob array
        # to make the transitions matrix you need to go to all of the pixels with nested loops and then set the array to what the function would say

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

        new_art = Bob_maker.compose_art(current_color="COLOR_1", art_length=HORIZONTAL_PIXELS*VERTICAL_PIXELS)
        """make the art with current color and length"""

        print("Writing song to file...") 
        """print something cool here"""

        img = Bob_maker.write_drawing(new_art)
        img.show()
        print("Process completed!")
if __name__ == "__main__":
        main()


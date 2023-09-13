
import numpy as np
from PIL import Image
# We can add more of these later...keeping it simple for now!
COLOR_CODES = {
"COLOR_1": [107, 174, 193],
"COLOR_2": [30,65,69],
"COLOR_3": [11,135,182],
"COLOR_4": [28,46,37],
"COLOR_5": [171,195,197],
"COLOR_6": [62,99,99],
"COLOR_7": [91,133,137],
"COLOR_8": [59,108,127],

}
HORIZONTAL_PIXELS = 25;
VERTICAL_PIXELS = 25;

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

    def compose_art(self, current_color="COLOR_1", art_length = HORIZONTAL_PIXELS*VERTICAL_PIXELS):
        index = 1
        artwork = np.zeros((HORIZONTAL_PIXELS, VERTICAL_PIXELS, 3), dtype=np.uint8)
        for row in range(HORIZONTAL_PIXELS):
            for col in range (VERTICAL_PIXELS):

                next_color = self.get_next_color(current_color)
                artwork [row, col] = COLOR_CODES[next_color]
                current_color = next_color
                index += 1
        return artwork



    def write_drawing(self, artwork):
        """turns  array into painting"""
        bobbyross = Image.fromarray(artwork, 'RGB')
        bobbyross.save('bobbyross.png')
        return bobbyross

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


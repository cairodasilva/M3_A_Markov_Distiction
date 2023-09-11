


import numpy as np
from PIL import Image
# We can add more of these later...keeping it simple for now!
COLOR_CODES = {
"COLOR_1": CODE,
"COLOR_2": CODE,
"COLOR_3": CODE,
"COLOR_4": CODE,
"COLOR_5": CODE,
"COLOR_6": CODE,
"COLOR_7": CODE,
"COLOR_8": CODE,
"COLOR_9": CODE,
"COLOR_10": CODE,
"COLOR_11": CODE,
"COLOR_12": CODE,
"COLOR_13": CODE,
"COLOR_14": CODE,
"COLOR_15": CODE,
}
HORIZONTAL_PIXELS = 640;
VERTICAL_PIXELS = 640;

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
    index = 0
    artwork = np.zeros((HORIZONTAL_PIXELS, VERTICAL_PIXELS, 3), dtype=np.uint8)
    while len(artwork) < art_length:
        next_color = self.get_next_color(current_color)
        artwork [HORIZONTAL_PIXELS/index, VERTICAL_PIXELS%index] = next_color
        current_color = next_color
        index += 1
    return artwork



def write_drawing(self, artwork):
    """turns  array into painting"""
    bobbyross = Image.fromarray(artwork, 'RGB')
    bobbyross.save(bobbyross.png)
    return bobbyross

def main():
    Bob_maker = MarkovBobRoss({
        "A": {"A": 0.3, "B": 0.4, "C": 0.3},
        "B": {"A": 0.7, "B": 0.2, "C": 0.1},
        "C": {"A": 0.1, "B": 0.7, "C": 0.2}

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


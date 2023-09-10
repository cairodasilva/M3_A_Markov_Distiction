


import numpy as np


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
class MarkovBobRoss:
def __init__(self, transition_matrix):

self.transition_matrix = transition_matrix
self.colors = list(transition_matrix.keys())
def get_next_color(self, current_note):

return np.random.choice(
self.colors,
p=[self.transition_matrix[current_color][next_color] \
for next_note in self.colors]
)
def compose_art(self, current_color="COLOR_1", art_length=3):
"""Generates a sequence of notes.
Args:
current_note (str): the note of the song that we are currently
looking at.
song_length (int): how many notes we should generate for the
song.
"""
artwork = []
while len(artwork) < art_length:
next_color = self.get_next_color(current_color)
artwork.append(next_color)
current_color = next_color
return artwork

def turn_to_2d(self):
    """figure out how to turn one array into 2d array of hex codes """
    return

def write_drawing(self):
    """turns 2d array into painting"""

def main():
Bob_Ross = MarkovBobRoss({
"A": {"A": 0.3, "B": 0.4, "C": 0.3},
"B": {"A": 0.7, "B": 0.2, "C": 0.1},
"C": {"A": 0.1, "B": 0.7, "C": 0.2}
"""make this actual"""
})
new_song = song_maker.compose_melody(current_note="C", song_length=10)
"""make the art with current color and length"""

print("Writing song to file...") 
"""print something cool here"""

song_maker.drawing(new_song)
print("Process completed!")
if __name__ == "__main__":
main()


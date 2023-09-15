# M3_A_Markov_Distiction
Title: It's Bob Ross if you squint really hard
Description
This is a collage generator that is inspired by Bob Ross's work and the elements  he uses. It uses multiple elements from multiple paintings that he uses. It then uses different probabilites to calculate the next image and then picks a random place on the canvs to put it. You can change the canvas size by changing the horizontal and vertical length in the initializing statements. This also changes the image size as each image takes up a even and proportional amount of the canvas compared to how many images there are. The amount of images can be changed in the main function udner num_images. This will shrink the images given a constant canvas size. 

Personal Meaning to Cairo
This relates to me on many aspects, the first being my connection to nature as I've spent all of my summers in college working in or around the outdoor industry such as working for a ski mountaineering guide company and spending last summer in Wanaka, New Zealand after I studied abroad working at a restarant and skiing everyday. In high school I worked on backcountry trail crews and have spent a lot of time and effort surrounding myself in nature. Bob Ross also had a netflix show when I was growing up and that was always playing throughout my life and has definetely contributed to my really easygoing and calm attitude towards things in life. This project allowed me combine both of those things I enjoy in my life using elements of nature taken from Bob Ross Paintings

Challenge
This was challening to me in a few ways, the first was that I had to go through multiple iterations to find something I liked (run TryThisToSeeSomeBadArt.py). Coming up with an idea that was unique to what I wanted and within the scope of my abilites definitely took a few tries. One big challenge I had was trying to figure out generating a matrix by itself. The matrix I had I wrote by hand, but on a few occasions I tried to generate a matrix of probabilites to come up with the position for the next image and couldn't really get the probabilites to line up how I wanted to there was a distribution that wasn't uniform. I think it would have been cool to try multiple order markov chains, while I understand how the probabilites work and how I could make a matrix with every combination P(x|a&b) where a and b are elements of the matrix, I couldn't really get around how to genreate a matrix that calculated that. I also struggled with the image processing to make the background transparent, so I have some room to improve.

Creativity
I personally do not think this is creative because it uses elements that already exist to make a collage and doesn't generate something on it's own. It feels like it gives the disguise of being creative, but I think for something to be creative there has to be an intent to solve a problem or explore something which I don't think this is. But it isn't entirely generative because it can come up with some cool collages that I couldn't reproduce

Credits
I asked multiple people in the class what they thought of my first go (pixel generator) and got mixed reviews of it's shock value
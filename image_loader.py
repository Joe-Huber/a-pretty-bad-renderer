import numpy as np
from PIL import Image

def load_image(path):
    image = Image.open(path)
    image.show()
    return image

def get_rgb(image):
    im = Image.open('image.gif')
    im_matrix = np.array(im)
    return im_matrix

def render(path):
    image = load_image(path)
    return get_rgb(image)
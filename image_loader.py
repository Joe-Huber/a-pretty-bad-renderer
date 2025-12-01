import numpy as np
from PIL import Image

def load_image(path):
    image = Image.open(path)
    return image

def get_rgb(image):
    im_matrix = np.array(image)
    return im_matrix

def render(path):
    image = load_image(path)
    return get_rgb(image)
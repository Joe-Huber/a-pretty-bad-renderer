# The main entry point for the program
# Takes an image and quality level as input.
from image_loader import render
from develop_modified_image import generate_new_image

image_path = "images/172x172.png"
quality_x = 100 # The quality of the image, based on how many columns there are

if __name__ == "__main__":
    img = render(image_path)
    generate_new_image(img, quality_x)
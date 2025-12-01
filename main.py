# The main entry point for the program
# Takes an image and quality level as input.
from image_loader import render
from develop_modified_image import generate_new_image
import matplotlib.pyplot as plt

image_path = "images/860x1033.png"
quality_x = 100 # The quality of the image, based on how many columns there are

if __name__ == "__main__":
    img = render(image_path)
    print(img)
    new_img = generate_new_image(img, quality_x)
    plt.imshow(new_img)
    plt.show()
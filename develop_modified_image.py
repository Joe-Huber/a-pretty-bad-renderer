import numpy as np
from rsa.common import ceil_div


def generate_new_image(og_img, new_x):
    #Generate the necessary components

    #Original dimensions
    og_dimensions = get_dimensions(og_img)
    og_x = og_dimensions[0]
    og_y = og_dimensions[1]

    new_y = int(og_y * new_x / og_x)

    #subspace dimensions for averaged pixels
    subspace_x = ceil_div(og_x, new_x)
    subspace_y = ceil_div(og_y, new_y)

    #The traversal sizes (how many spots to move in loop)

    #X traversal
    if og_x % new_x == 0:
        traversal_x = subspace_x
    else:
        traversal_x = subspace_x -1

    #Y traversal
    if og_y % new_y == 0:
        traversal_y = subspace_y
    else:
        traversal_y = subspace_y -1

    new_img = np.zeros([new_y, new_x])

    og_x_ind = 0
    og_y_ind = 0

    for y in range(new_y):
        for x in range(new_x):
            print(f"Processing pixel at ({x}, {y})")
            og_x_ind += traversal_x
        og_x_ind = 0
        og_y_ind += traversal_y


def get_dimensions(arr):
    return [len(arr), len(arr[0])]
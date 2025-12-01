import numpy as np
from rsa.common import ceil_div


def generate_new_image(og_img, new_width):
    #Generate the necessary components

    #Original dimensions
    og_dimensions = get_dimensions(og_img)
    og_height = og_dimensions[0]
    og_width = og_dimensions[1]

    new_height = int(og_height * new_width / og_width)

    #subspace dimensions for averaged pixels
    subspace_width = ceil_div(og_width, new_width)
    subspace_height = ceil_div(og_height, new_height)

    new_img = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    for y in range(new_height):
        og_row_ind = int(y * og_height / new_height)
        for x in range(new_width):
            og_col_ind = int(x * og_width / new_width)
            new_img[y][x] = average_pixels(generate_subspace(og_img, og_col_ind, og_row_ind, subspace_width, subspace_height))
    return new_img


def get_dimensions(arr):
    return [len(arr), len(arr[0])]

def generate_subspace(arr, x, y, width, length):
    subspace = []
    og_height = len(arr)
    if og_height == 0:
        return np.array(subspace)
    og_width = len(arr[0])

    y_end = min(y + length, og_height)
    x_end = min(x + width, og_width)

    for i in range(y, y_end):
        row = arr[i][x:x_end]
        subspace.append(row)
    
    return subspace

def average_pixels(lis):
    # This way is valuing the RGB values, no curve applied
    r_total = np.int64(0)
    g_total = np.int64(0)
    b_total = np.int64(0)
    pixel_count = 0
    for row in lis:
        for pixel in row:
            r_total += pixel[0]
            g_total += pixel[1]
            b_total += pixel[2]
            pixel_count += 1
    
    if pixel_count == 0:
        return [0, 0, 0]

    return [int(r_total / pixel_count), int(g_total / pixel_count), int(b_total / pixel_count)]

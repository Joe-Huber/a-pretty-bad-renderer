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

    new_img = np.zeros((new_y, new_x, 3), dtype=np.uint8)

    og_x_ind = 0
    og_y_ind = 0

    for y in range(new_y):
        for x in range(new_x):
            new_img[y][x] = average_pixels(generate_subspace(og_img, og_x_ind, og_y_ind, subspace_x, subspace_y))
            og_x_ind += traversal_x
        og_x_ind = 0
        og_y_ind += traversal_y
    print(new_img)


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

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


def get_dimensions(arr):
    return [len(arr), len(arr[0])]
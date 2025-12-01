from rsa.common import ceil_div


def generate_new_image(og_img, new_x):
    og_dimensions = get_dimensions(og_img)
    og_x = og_dimensions[0]
    og_y = og_dimensions[1]
    subspace_size = ceil_div(og_x, new_x)
    if og_x % new_x == 0:
        traversal_length = subspace_size
    else:
        traversal_length = subspace_size - 1
def get_dimensions(arr):
    return [len(arr), len(arr[0])]
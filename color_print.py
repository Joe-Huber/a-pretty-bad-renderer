from colorama import init, Fore, Style

def print_colored_image(image_data):
    """
    Prints a 2D array of RGB values to the console as a colored image.

    Each pixel is represented by a '█' character, and its color is set
    using the corresponding RGB value from the input array.

    Args:
        image_data (list of lists of tuples): A 2D list where each element
                                              is an RGB tuple (r, g, b).
    """
    init()
    try:
        for row in image_data:
            for r, g, b in row:
                # Set the foreground color using 24-bit ANSI escape codes
                print(f"\x1b[38;2;{r};{g};{b}m█", end="")
            print()  # Newline after each row
    finally:
        # Reset the color and deinitialize colorama
        print(Style.RESET_ALL)

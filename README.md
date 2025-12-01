# A Pretty Bad Renderer

This project is a simple image renderer that takes an image file, resizes it to a specified quality, and then prints it to the console using colored ASCII characters.

## How to Run

1.  **Install dependencies:**
    *   `numpy`
    *   `colorama`
    *   `matplotlib`
    *   `Pillow` (PIL)

2.  **Place your image:**
    *   Put the image you want to render in the `images` directory.

3.  **Configure `main.py`:**
    *   Open `main.py` and set the `image_path` variable to the path of your image.
    *   Adjust the `quality_x` variable to control the width of the output image.

4.  **Run the program:**
    ```bash
    python main.py
    ```

## Project Structure

*   `main.py`: The main entry point for the program. It loads an image, generates a new one with a specified quality, and prints it to the console.
*   `image_loader.py`: Contains the `render` function, which loads an image from a file path and returns it as a NumPy array.
*   `develop_modified_image.py`: Contains the logic for resizing the image. The `generate_new_image` function takes an image and a new width, and generates a new, resized image.
*   `color_print.py`: Contains the `print_colored_image` function, which takes a 2D array of RGB values and prints it to the console using colored ASCII characters.
*   `images/`: A directory to store your images.

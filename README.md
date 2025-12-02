<div align="center">
  <h1 align="center">A Pretty Bad Renderer</h1>
  <p align="center">
    A simple Python script to render images in your terminal.
  </p>
  <p align="center">
    <a href="https://github.com/joe-huber/a-pretty-bad-renderer/blob/main/LICENSE">
      <img alt="License" src="https://img.shields.io/github/license/joe-huber/a-pretty-bad-renderer">
    </a>
    <a href="https://github.com/joe-huber/a-pretty-bad-renderer/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/joe-huber/a-pretty-bad-renderer">
    </a>
    <a href="https://github.com/joe-huber/a-pretty-bad-renderer/network/members">
      <img alt="Forks" src="https://img.shields.io/github/forks/joe-huber/a-pretty-bad-renderer">
    </a>
    <a href="https://github.com/joe-huber/a-pretty-bad-renderer/stargazers">
      <img alt="Stars" src="https://img.shields.io/github/stars/joe-huber/a-pretty-bad-renderer">
    </a>
  </p>
</div>

---

This project is a simple image renderer that takes an image file, resizes it to a specified quality, and then prints it to the console using colored ASCII block characters.

## ✨ Features

*   **Image to ASCII:** Converts standard image files into a terminal-based representation.
*   **Color Support:** Uses `colorama` to render the image with 24-bit RGB colors.
*   **Custom Quality:** Easily adjust the output width of the rendered image.

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3 installed on your system.

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/joe-huber/a-pretty-bad-renderer.git
    cd a-pretty-bad-renderer
    ```

2.  Install the required dependencies:
    ```bash
    pip install numpy colorama matplotlib pillow
    ```

## Usage

1.  **Add your image:**
    *   Place the image you want to render inside the `images/` directory.

2.  **Configure the script:**
    *   Open `main.py` and update the following variables:
        *   `image_path`: Set this to the path of your image (e.g., `"images/my-image.png"`).
        *   `quality_x`: Adjust this number to control the width (in characters) of the output image.

3.  **Run it:**
    ```bash
    python3 main.py
    ```

    You will see your image rendered in the terminal!

## Project Structure

```
.
├── main.py                  # Main script to run the renderer
├── image_loader.py          # Handles loading the image file
├── develop_modified_image.py  # Core logic for image resizing
├── color_print.py           # Handles the terminal output
├── images/                    # Directory for your images
└── README.md                # You are here!
```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

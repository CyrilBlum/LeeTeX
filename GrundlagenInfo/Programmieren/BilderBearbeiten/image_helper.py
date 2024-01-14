from PIL import Image
import random
from bs4 import BeautifulSoup


# Monochrome Bilder
def load_bw_pixels(filename):
    im = Image.open(filename)
    im = im.convert("1")
    L = list(im.getdata())
    return [1 if 255 == i else 0 for i in L]


def load_bw_pixels_2d(filename):
    im = load_bw_image(filename)
    w, h = im.size
    data = im.getdata()
    return [[data[y * w + x] for y in range(h)] for x in range(w)]


def load_bw_image(filename):
    im = Image.open(filename)
    return im.convert("1")


def new_bw_pixels_2d(w, h):
    return [[0 for y in range(h)] for x in range(w)]


def new_bw_image(w, h, pixels=None):
    im = Image.new("1", (w, h))
    if pixels is not None:
        if isinstance(pixels[0], list):
            pixels = list(zip(*pixels))
            pixels = [item for sublist in pixels for item in sublist]
        im.putdata(pixels)
    return im


# Graustufen
def load_grayscale_image(filename):
    im = Image.open(filename)
    return im.convert("L")


def load_grayscale_pixels(filename):
    im = load_grayscale_image(filename)
    return list(im.getdata())


def load_grayscale_pixels_2d(filename):
    im = load_grayscale_image(filename)
    w, h = im.size
    data = im.getdata()
    return [[data[y * w + x] for y in range(h)] for x in range(w)]


def new_grayscale_pixels_2d(w, h):
    return [[0 for y in range(h)] for x in range(w)]


def new_grayscale_image(w, h, pixels=None):
    im = Image.new("L", (w, h))
    if pixels is not None:
        if isinstance(pixels[0], list):
            pixels = list(zip(*pixels))
            pixels = [item for sublist in pixels for item in sublist]
        im.putdata(pixels)
    return im


# RGB
def load_rgb_image(filename):
    im = Image.open(filename)
    return im.convert("RGB")


def load_rgb_pixels_2d(filename):
    im = Image.open(filename)
    w, h = im.size
    data = im.getdata()
    return [[data[y * w + x] for y in range(h)] for x in range(w)]


def load_rgb_pixels(filename):
    im = load_rgb_image(filename)
    return list(im.getdata())


def new_rgb_pixels_2d(w, h):
    return [[(0, 0, 0) for y in range(h)] for x in range(w)]


def new_rgb_image(w, h, pixels=None):
    im = Image.new("RGB", (w, h))
    if pixels is not None:
        if isinstance(pixels[0], list):
            pixels = list(zip(*pixels))
            pixels = [item for sublist in pixels for item in sublist]
        im.putdata(pixels)
    return im


# Misc:
def random_pixel_value():
    return random.randint(0, 255)


# Display Helper:
def show_images_vertically(im1, im2):
    dst = Image.new("RGB", (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    dst.show()


def update_html_file(file_path, target_string, new_string):
    # Read the HTML file
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the target string and update it
    target_element = soup.find(string=lambda text: target_string in str(text))
    if target_element:
        target_element.replace_with(new_string)

        # Save the updated HTML content back to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(str(soup))
        print(
            f'Successfully updated "{target_string}" to "{new_string}" in {file_path}'
        )
    else:
        print(f'Error: "{target_string}" not found in {file_path}')


# Example usage
update_html_file("path/to/your/file.html", "old_string", "new_string")

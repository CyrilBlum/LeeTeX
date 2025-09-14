import random
from PIL import Image

# -------------------------------------------------
# Image processing utilities (BW, Grayscale, RGB)
# -------------------------------------------------

def _flatten_2d(pixels_2d):
    """Flatten a 2D list into a 1D list (row-major order)."""
    return [pixel for row in pixels_2d for pixel in row]


def _transpose_2d(pixels_2d):
    """Transpose a 2D list."""
    return [list(row) for row in zip(*pixels_2d)]


### Black & White Images ###
def get_bw_image(filename):
    """Open image and convert to black & white (mode '1')."""
    return Image.open(filename).convert("1")


def get_1d_bw(filename):
    """Return 1D binary list of pixels (0=black, 1=white)."""
    im = get_bw_image(filename)
    return [1 if i == 255 else 0 for i in im.getdata()]


def get_2d_bw(filename):
    """Return 2D binary list of pixels (0=black, 1=white)."""
    im = get_bw_image(filename)
    w, h = im.size
    data = list(im.getdata())
    return [[data[y * w + x] for x in range(w)] for y in range(h)]


def generate_bw_image(w, h, pixels=None):
    """Generate BW image. Pixels can be 1D or 2D."""
    im = Image.new("1", (w, h))
    if pixels is not None:
        if isinstance(pixels[0], list):
            pixels = _flatten_2d(pixels)
        im.putdata(pixels)
    return im


### Grayscale Images ###
def get_grayscale_image(filename):
    return Image.open(filename).convert("L")


def get_1d_grayscale(filename):
    return list(get_grayscale_image(filename).getdata())


def get_2d_grayscale(filename):
    im = get_grayscale_image(filename)
    w, h = im.size
    data = list(im.getdata())
    return [[data[y * w + x] for x in range(w)] for y in range(h)]


def generate_grayscale_image(w, h, pixels=None):
    im = Image.new("L", (w, h))
    if pixels is not None:
        if isinstance(pixels[0], list):
            pixels = _flatten_2d(pixels)
        im.putdata(pixels)
    return im


### RGB Images ###
def get_rgb_image(filename):
    return Image.open(filename).convert("RGB")


def get_1d_rgb(filename):
    return list(get_rgb_image(filename).getdata())


def get_2d_rgb(filename):
    im = get_rgb_image(filename)
    w, h = im.size
    data = list(im.getdata())
    return [[data[y * w + x] for x in range(w)] for y in range(h)]


def generate_rgb_image(w, h, pixels=None):
    im = Image.new("RGB", (w, h))
    if pixels is not None:
        if isinstance(pixels[0], list):
            pixels = _flatten_2d(pixels)
        im.putdata(pixels)
    return im


### Utility Functions ###
def init_zeros_2d(w, h, mode="BW"):
    """Initialize a 2D zero array for BW, Grayscale, or RGB."""
    if mode == "RGB":
        return [[(0, 0, 0) for _ in range(w)] for _ in range(h)]
    else:
        return [[0 for _ in range(w)] for _ in range(h)]


def get_random_pixel_value():
    return random.randint(0, 255)


def compare_two_images(im1, im2):
    """Show two images side by side for comparison."""
    dst = Image.new("RGB", (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    dst.show()
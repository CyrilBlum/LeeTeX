from PIL import Image
import random


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

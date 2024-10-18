import random

from PIL import Image

# consider the documentation of the 'Image' module
# of the pillow (PIL Fork) library:
# https://pillow.readthedocs.io/en/stable/reference/Image.html


### black and white (bw) images ###
def get_bw_image(filename):
    # open the given file as a pillow image object
    im = Image.open(filename)
    return im.convert("1")


def get_1d_bw(filename):
    # returns a binary (black / white) 1d-list of all the pixels of the image given by 'filename'
    im = Image.open(filename)
    im = im.convert("1")
    l = list(im.getdata())
    return [1 if 255 == i else 0 for i in l]


def get_2d_bw(filename):
    # returns a binary (black / white) 2d-list of all the pixels of the image given by 'filename'
    im = load_bw_image(filename)
    w, h = im.size
    data = im.getdata()
    return [[data[y * w + x] for y in range(h)] for x in range(w)]


def init_zeros_2d_bw_gray(w, h):
    # returns a zero-initialized 2d-list with given dimensions (width / height)
    # this 2d-list can hold black / white as well as grayscale values
    return [[0 for y in range(h)] for x in range(w)]


def generate_bw_image(w, h, pixels=None):
    # generates a black / white image with given dimensions (width / height)
    # the optional argument 'pixels' (either 1d-list or 2d-list)
    # is used to define the pixel values of the returned image
    im = Image.new("1", (w, h))
    if pixels is not None:
        if isinstance(pixels[0], list):
            # if 'pixels' is a 2d-list, we need to perform a small transformation first
            pixels = list(zip(*pixels))
            pixels = [item for sublist in pixels for item in sublist]
        im.putdata(pixels)
    return im


### grayscale images ###
def get_grayscale_image(filename):
    im = Image.open(filename)
    return im.convert("L")


def get_1d_grayscale(filename):
    im = get_grayscale_image(filename)
    return list(im.getdata())


def get_2d_grayscale(filename):
    im = get_grayscale_image(filename)
    w, h = im.size
    data = im.getdata()
    return [[data[y * w + x] for y in range(h)] for x in range(w)]


def generate_grayscale_image(w, h, pixels=None):
    im = Image.new("L", (w, h))
    if pixels is not None:
        if isinstance(pixels[0], list):
            pixels = list(zip(*pixels))
            pixels = [item for sublist in pixels for item in sublist]
        im.putdata(pixels)
    return im


### RGB images ###
def get_rgb_image(filename):
    im = Image.open(filename)
    return im.convert("RGB")


def get_1d_rgb(filename):
    im = get_rgb_image(filename)
    return list(im.getdata())


def get_2d_rgb(filename):
    im = Image.open(filename)
    w, h = im.size
    data = im.getdata()
    return [[data[y * w + x] for y in range(h)] for x in range(w)]


def init_zeros_2d_rgb(w, h):
    return [[(0, 0, 0) for y in range(h)] for x in range(w)]


def generate_rgb_image(w, h, pixels=None):
    im = Image.new("RGB", (w, h))
    if pixels is not None:
        if isinstance(pixels[0], list):
            pixels = list(zip(*pixels))
            pixels = [item for sublist in pixels for item in sublist]
        im.putdata(pixels)
    return im


### general utility functions ###
def get_random_pixel_value():
    return random.randint(0, 255)


def compare_two_images(im1, im2):
    dst = Image.new("RGB", (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    dst.show()

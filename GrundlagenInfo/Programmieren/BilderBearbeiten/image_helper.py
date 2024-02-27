from PIL import Image
import random


## monochrome images (black / white only) ##


def load_monochrome_image(image_name):
    im = Image.open(image_name)
    return im.convert("1")


def load_monochrome_pixels(image_name):
    im = load_monochrome_image(image_name)
    L = list(im.getdata())
    return [1 if 255 == i else 0 for i in L]


## grayscale images ##
def load_grayscale_image(image_name):
    im = Image.open(image_name)
    return im.convert("L")


def load_grayscale_pixels(image_name):
    im = load_grayscale_image(image_name)
    return list(im.getdata())


## rgb images ##
def load_rgb_image(image_name):
    im = Image.open(image_name)
    return im.convert("rgb")


def load_rgb_pixels(image_name):
    im = load_rgb_image(image_name)
    return list(im.getdata())


## universal utility ##
# create new zero initialized 2d list of lists
def new_pixels_2d(width, height):
    return [[0] * height] * width


# load image as 2d list of lists
def load_pixels_2d(image_name):
    im = load_monochrome_image(image_name)
    width, height = im.size
    data = im.getdata()
    return [[data[y * width + x] for y in range(height)] for x in range(width)]


# load image as 1d list of pixels
def load_pixels_1d(image_name, mode):
    if mode == "monochrome":
        load_monochrome_pixels(image_name)
    elif mode == "grayscale":
        load_grayscale_pixels(image_name)
    elif mode == "rgb":
        load_rgb_pixels(image_name)
    else:
        print("Error: invalide mode (choose either: monochrome, grayscale or color)")


def new_image(width, height, mode):
    if mode == "monochrome":
        return Image.new("1", (width, height))
    elif mode == "grayscale":
        return Image.new("L", (width, height))
    elif mode == "rgb":
        return Image.new("rgb", (width, height))
    else:
        print("Error: invalide mode (choose either: monochrome, grayscale or color)")


def random_pixel_value():
    return random.randint(0, 255)


# show two images side by side to compare them
def compare_images(im1, im2):
    dst = Image.new("rgb", (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    dst.show()


# def new_rgb_image(w, h, pixels=None):
#     im = Image.new("rgb", (w, h))
#     if pixels is not None:
#         if isinstance(pixels[0], list):
#             pixels = list(zip(*pixels))
#             pixels = [item for sublist in pixels for item in sublist]
#         im.putdata(pixels)
#     return im

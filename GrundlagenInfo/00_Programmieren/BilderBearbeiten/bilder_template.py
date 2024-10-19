import math
import random

import image_helper as ih


### Schwarzweissbilder ###
# Aufgabe 1
def count_black_pixels(filename):
    # counts and returns the number of black pixels
    # of a given black / white image

    # get an 1d list of the image's pixel values
    pixel_list = ih.get_1d_bw(filename)

    # initialize the counter
    num_black_pixels = 0

    # loop through the list and count the pixels with
    # value 0 (those are the black pixels)
    for pixel in pixel_list:
        if pixel == 0:
            # increment counter if a black pixel is found
            ...
            ...
    return num_black_pixels


# Aufgabe 2
def invert_black_white_image(filename):

    # load original image as pillow image object
    original_image = ih.get_bw_image(filename)

    # get an 1d list of the image's pixel values
    original_pixel_list = ih.get_1d_bw(filename)

    # initialize empty list
    transformed_pixel_list = []

    # append black pixels as white pixels and vice versa
    # to built the transformed pixel list pixel by pixel
    for pixel in original_pixel_list:
        ...
        ...

    # get dimensions of original image
    w, h = original_image.size

    # generate an image with the same dimensions as the original image
    # but with transformed pixel values
    transformed_image = ih.generate_bw_image(w, h, transformed_pixel_list)

    # compare the original vs the transformed image side by side
    ih.compare_two_images(original_image, transformed_image)


# Aufgabe 3
def random_black_white_image(width, height):
    pixel_list_random_bits = []

    number_of_bits = ...

    for _ in range(number_of_bits):
        random_bit = random.randint(0, 1)
        ...

    random_image = ih.generate_bw_image(width, height, pixel_list_random_bits)
    random_image.show()


### Graustufenbilder ###
# Aufgabe 4
def invert_grayscale_image(filename):
    # load original image as pillow image object
    original_image = ih.get_grayscale_image(filename)

    # get an 1d list of the image's pixel values
    original_pixel_list = ih.get_1d_grayscale(filename)

    # initialize empty list
    transformed_pixel_list = []

    # invert every single pixel (0 <-> 255, 1 <-> 254, 2 <-> 253)
    # can you find a simple mathematical transformation to perfom this transformation?
    for pixel in original_pixel_list:
        ...
        ...

    # get dimensions of original image
    w, h = original_image.size

    # generate an image with the same dimensions as the original image
    # but with transformed pixel values
    transformed_image = ih.generate_grayscale_image(
        w, h, transformed_pixel_list
    )

    # compare the original vs the transformed image side by side
    ih.compare_two_images(original_image, transformed_image)


# Aufgabe 5
def only_8_shades_of_gray(filename):
    # load original image as pillow image object
    original_image = ih.get_grayscale_image(filename)

    # get an 1d list of the image's pixel values
    original_pixel_list = ih.get_1d_grayscale(filename)

    # initialize empty list
    transformed_pixel_list = []

    # out of the 8 shades of gray, find the correct shade (group) for each pixel in the image
    for pixel in original_pixel_list:
        ...
        ...

    # get dimensions of original image
    w, h = original_image.size

    # generate an image with the same dimensions as the original image
    # but with transformed pixel values
    transformed_image = ih.generate_grayscale_image(
        w, h, transformed_pixel_list
    )

    # compare the original vs the transformed image side by side
    ih.compare_two_images(original_image, transformed_image)


### RGB-Bilder ###
# Aufgabe 6
def increase_green(filename):
    # load original image as pillow image object
    original_image = ih.get_rgb_image(filename)

    # get an 1d list of the image's pixel values
    original_pixel_list = ih.get_1d_rgb(filename)

    # initialize empty list
    transformed_pixel_list = []

    for r, g, b in original_pixel_list:
        ...
        pixel = (int(r), int(g), int(b))
        ...

    # get dimensions of original image
    w, h = original_image.size

    # generate an image with the same dimensions as the original image
    # but with transformed pixel values
    transformed_image = ih.generate_rgb_image(w, h, transformed_pixel_list)

    # compare the original vs the transformed image side by side
    ih.compare_two_images(original_image, transformed_image)


# Aufgabe 7
def sepia_filter(filename):
    # load original image as pillow image object
    original_image = ih.get_rgb_image(filename)

    # get an 1d list of the image's pixel values
    original_pixel_list = ih.get_1d_rgb(filename)

    # initialize empty list
    transformed_pixel_list = []

    for r, g, b in original_pixel_list:
        ...
        ...
        ...
        ...
        ...

    # get dimensions of original image
    w, h = original_image.size

    # generate an image with the same dimensions as the original image
    # but with transformed pixel values
    transformed_image = ih.generate_rgb_image(w, h, transformed_pixel_list)

    # compare the original vs the transformed image side by side
    ih.compare_two_images(original_image, transformed_image)


### Weitere Aufgaben ###
# Aufgabe 8
def vertical_stripes(filename):
    # load original image as pillow image object
    original_image = ih.get_grayscale_image(filename)

    # get an 1d list of the image's pixel values
    original_pixel_list = ih.get_1d_grayscale(filename)

    # initialize empty list
    transformed_pixel_list = []

    # get dimensions of original image
    w, h = original_image.size

    ...
    ...
    ...
    ...
    ...
    ...
    ...

    # generate an image with the same dimensions as the original image
    # but with transformed pixel values
    transformed_image = ih.generate_grayscale_image(
        w, h, transformed_pixel_list
    )

    # compare the original vs the transformed image side by side
    # ih.compare_two_images(original_image, transformed_image)
    transformed_image.show()


# Aufgabe 9
# helper function
def is_prime(number):
    # returns 'True' if 'number' is a prime number and 'False' otherwise
    ...
    ...
    ...
    ...
    ...
    ...


def plot_primes(width, height):
    pixel_list_primes = []

    number_of_bits = ...

    for index in range(number_of_bits):
        ...
        ...
        ...
        ...

    random_image = ih.generate_bw_image(width, height, pixel_list_primes)
    random_image.show()


### calling our functions ###
# print(count_black_pixels("ivy_bw.jpg"))  # Aufgabe 1
# invert_black_white_image("ivy_bw.jpg")  # Aufgabe 2
# random_black_white_image(1000, 600)  # Aufgabe 3
# invert_grayscale_image("ivy_gray.jpg")  # Aufgabe 4
# only_8_shades_of_gray("ivy_gray.jpg")  # Aufgabe 5
# increase_green("ivy_rgb.jpg") # Aufgabe 6
# sepia_filter("effi_rgb.jpg") # Aufgabe 7
# vertical_stripes("ivy_gray.jpg")  # Aufgabe 8
# plot_primes(200, 200)

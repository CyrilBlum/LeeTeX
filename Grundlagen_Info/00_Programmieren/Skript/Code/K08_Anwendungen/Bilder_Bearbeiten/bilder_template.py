import math
import random
import image_helper as ih


### ------------------------- ###
### Schwarz-Weiss-Bilder       ###
### ------------------------- ###


def count_black_pixels(filename):
    """Zählt die schwarzen Pixel eines Schwarz-Weiss-Bildes."""
    pixel_list = ih.get_1d_bw(filename)
    num_black_pixels = 0
    for p in pixel_list:
        if p == 0:
            num_black_pixels += 1
    return num_black_pixels


def invert_black_white_image(filename):
    """Invertiert ein Schwarz-Weiss-Bild und zeigt es neben dem Original."""
    original_image = ih.get_bw_image(filename)
    pixels = ih.get_1d_bw(filename)

    inverted_pixels = []
    for p in pixels:
        ...
        ...
        ...

    w, h = original_image.size
    transformed_image = ih.generate_bw_image(w, h, inverted_pixels)
    ih.compare_two_images(original_image, transformed_image)


def random_black_white_image(width, height):
    """Erzeugt ein zufälliges Schwarz-Weiss-Bild mit gegebener Breite und Höhe."""
    pixels = []
    for _ in range(...):
        pixels.append(...)
    random_image = ih.generate_bw_image(width, height, pixels)
    random_image.show()


### ------------------------- ###
### Graustufen-Bilder          ###
### ------------------------- ###


def invert_grayscale_image(filename):
    """Invertiert ein Graustufenbild (0 <-> 255) und zeigt es neben dem Original."""
    original_image = ih.get_grayscale_image(filename)
    pixels = ih.get_1d_grayscale(filename)

    inverted_pixels = []
    for p in pixels:
        ...

    w, h = original_image.size
    transformed_image = ih.generate_grayscale_image(w, h, inverted_pixels)
    ih.compare_two_images(original_image, transformed_image)


def only_8_shades_of_gray(filename):
    """Reduziert ein Graustufenbild auf 8 Graustufen."""
    original_image = ih.get_grayscale_image(filename)
    pixels = ih.get_1d_grayscale(filename)

    transformed_pixels = []
    for p in pixels:
        ...
        ...

    w, h = original_image.size
    transformed_image = ih.generate_grayscale_image(w, h, transformed_pixels)
    ih.compare_two_images(original_image, transformed_image)


def vertical_stripes(filename, stripe_width=2, gap=5):
    """Erzeugt vertikale schwarze Streifen in einem Graustufenbild."""
    original_image = ih.get_grayscale_image(filename)
    pixels = ih.get_1d_grayscale(filename)
    w, h = original_image.size

    transformed_pixels = []
    for i in range(...):
        ...
        ...

    transformed_image = ih.generate_grayscale_image(w, h, transformed_pixels)
    transformed_image.show()


### ------------------------- ###
### RGB-Bilder                 ###
### ------------------------- ###


def increase_green(filename, factor=1.2):
    """Erhöht den Grün-Kanal eines RGB-Bildes um den gegebenen Faktor."""
    original_image = ih.get_rgb_image(filename)
    pixels = ih.get_1d_rgb(filename)

    transformed_pixels = []
    for r, g, b in pixels:
        g_new = ...
        transformed_pixels.append((r, g_new, b))

    w, h = original_image.size
    transformed_image = ih.generate_rgb_image(w, h, transformed_pixels)
    ih.compare_two_images(original_image, transformed_image)


def sepia_filter(filename):
    """Wendet einen Sepia-Filter auf ein RGB-Bild an."""
    original_image = ih.get_rgb_image(filename)
    pixels = ih.get_1d_rgb(filename)

    transformed_pixels = []
    for r, g, b in pixels:
        tr = ...
        tg = ...
        tb = ...
        transformed_pixels.append((tr, tg, tb))

    w, h = original_image.size
    transformed_image = ih.generate_rgb_image(w, h, transformed_pixels)
    ih.compare_two_images(original_image, transformed_image)


### ------------------------- ###
### Weitere Aufgaben           ###
### ------------------------- ###


def is_prime(number):
    """Prüft, ob eine Zahl eine Primzahl ist."""
    if number < 2:
        return False
    for k in range(2, int(math.sqrt(number)) + 1):
        ...
        ...
    return True


def plot_primes(width, height):
    """Erzeugt ein Schwarz-Weiss-Bild, bei dem Primzahlen schwarze Pixel darstellen."""
    pixels = []
    for i in range(...):
        if is_prime(i):
            ...
        else:
            ...

    image = ih.generate_bw_image(width, height, pixels)
    image.show()


### ------------------------- ###

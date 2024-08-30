import image_helper as ih


def count_black_pixels(filename):
    # count and return the number of black pixels
    # of a given black / white image

    pixel_list = ih.load_bw_pixels(filename)
    black_pixels = 0

    for pixel in pixel_list:
        if pixel == 0:
            black_pixels += 1

    return black_pixels


def invert_black_white_image(filename):
    original = ih.load_bw_image(filename)
    pixel_list = ih.load_bw_pixels(filename)

    inverted = []
    for pixel in pixel_list:
        if pixel == 0:
            inverted.append(1)
        else:
            inverted.append(0)

    w, h = original.size
    inverted_image = ih.new_bw_image(w, h, inverted)
    ih.compare_images(original, inverted_image)


invert_black_white_image("Effretikon_Black_White.jpg")

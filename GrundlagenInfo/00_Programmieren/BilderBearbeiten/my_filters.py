import image_helper as ih


def count_black_pixels(filename):
    # count and return the number of black pixels
    # of a given black / white image
    pixel_list = ih.get_1d_bw(filename)
    num_black_pixels = 0

    for pixel in pixel_list:
        if pixel == 0:
            num_black_pixels += 1

    return num_black_pixels


def invert_black_white_image(filename):
    original_image = ih.get_bw_image(filename)
    original_pixel_list = ih.get_1d_bw(filename)
    inverted_pixel_list = []

    for pixel in original_pixel_list:
        if pixel == 0:
            inverted_pixel_list.append(1)
        else:
            inverted_pixel_list.append(0)

    w, h = original_image.size
    inverted_image = ih.generate_bw_image(w, h, inverted_pixel_list)
    ih.compare_two_images(original_image, inverted_image)


print(count_black_pixels("ivy_bw.jpg"))
invert_black_white_image("ivy_bw.jpg")

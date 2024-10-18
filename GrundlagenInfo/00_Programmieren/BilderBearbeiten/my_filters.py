import image_helper as ih


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
            num_black_pixels += 1

    return num_black_pixels


def invert_black_white_image(filename):

    # load original image as pillow image object
    original_image = ih.get_bw_image(filename)

    # get an 1d list of the image's pixel values
    original_pixel_list = ih.get_1d_bw(filename)

    # initialize empty list
    inverted_pixel_list = []

    # append black pixels as white pixels and vice versa
    # to built the inverted pixel list pixel by pixel
    for pixel in original_pixel_list:
        if pixel == 0:
            inverted_pixel_list.append(1)
        else:
            inverted_pixel_list.append(0)

    # get dimensions of original image
    w, h = original_image.size

    # generate an image with the same dimensions as the original image
    # but with inverted pixel values
    inverted_image = ih.generate_bw_image(w, h, inverted_pixel_list)

    # compare the original vs the inverted image side by side
    ih.compare_two_images(original_image, inverted_image)


print(count_black_pixels("ivy_bw.jpg"))
invert_black_white_image("ivy_bw.jpg")

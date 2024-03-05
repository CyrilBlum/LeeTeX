import image_helper as ih


# def count_black_pixels(image):
#     # count and return the number of black pixels
#     # of a given black / white image
#
#     pixel_list = ih.load_bw_pixels(image)
#     black_pixels = 0
#
#     for pixel in pixel_list:
#         if pixel == 0:
#             black_pixels += 1
#
#     return black_pixels
#
#
# def invert_black_white_image(image):
#     inverted = []
#     pixel_list = ih.load_bw_pixels(image)
#
#     for pixel in pixel_list:
#         if pixel == 0:
#             inverted.append(1)
#         else:
#             inverted.append(0)
#
#     w, h = image.size
#     inverted_image = ih.new_bw_image(w, h, inverted)
#     ih.show_images_vertically(image, inverted_image)


# print(count_black_pixels("Ivy_Black_White.jpg"))

# im = ih.Image.open("Ivy_Color.jpeg")
# im = im.convert("1")
# print(im.getdata()[0])

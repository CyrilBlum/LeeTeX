from time import time

import matplotlib.pyplot as plt
import numpy as np
from numba import jit


# JIT-compiled Mandelbrot iteration function
@jit(nopython=True)
def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter


# Generate the Mandelbrot set
@jit(nopython=True, parallel=True)
def generate_mandelbrot(
    width, height, re_start, re_end, im_start, im_end, max_iter
):
    image = np.zeros((height, width), dtype=np.float32)
    for x in range(width):
        for y in range(height):
            re = re_start + (x / width) * (re_end - re_start)
            im = im_start + (y / height) * (im_end - im_start)
            c = complex(re, im)
            image[y, x] = mandelbrot(c, max_iter)
    return image


# Configuration
width, height = 15360, 8640  # 16K resolution
re_start, re_end = -2.0, 1.0
im_start, im_end = -1.0, 1.0
max_iter = 500

# Timing and execution
print("Generating Mandelbrot set...")
start = time()
image = generate_mandelbrot(
    width, height, re_start, re_end, im_start, im_end, max_iter
)
end = time()
print(f"Done in {end - start:.2f} seconds.")

# Save the image
output_file = "mandelbrot_16k_hsv.png"
plt.imsave(output_file, image, cmap="hsv")
print(f"Saved image to {output_file}")

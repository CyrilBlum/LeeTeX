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
        if p == 0:
            inverted_pixels.append(1)
        else:
            inverted_pixels.append(0)

    w, h = original_image.size
    transformed_image = ih.generate_bw_image(w, h, inverted_pixels)
    ih.compare_two_images(original_image, transformed_image)


def random_black_white_image(width, height):
    """Erzeugt ein zufälliges Schwarz-Weiss-Bild mit gegebener Breite und Höhe."""
    pixels = []
    for _ in range(width * height):
        pixels.append(random.randint(0, 1))
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
        inverted_pixels.append(255 - p)

    w, h = original_image.size
    transformed_image = ih.generate_grayscale_image(w, h, inverted_pixels)
    ih.compare_two_images(original_image, transformed_image)


def only_8_shades_of_gray(filename):
    """Reduziert ein Graustufenbild auf 8 Graustufen."""
    original_image = ih.get_grayscale_image(filename)
    pixels = ih.get_1d_grayscale(filename)

    transformed_pixels = []
    for p in pixels:
        shade = (p // 32) * 32
        transformed_pixels.append(shade)

    w, h = original_image.size
    transformed_image = ih.generate_grayscale_image(w, h, transformed_pixels)
    ih.compare_two_images(original_image, transformed_image)


def vertical_stripes(filename, stripe_width=2, gap=5):
    """Erzeugt vertikale schwarze Streifen in einem Graustufenbild."""
    original_image = ih.get_grayscale_image(filename)
    pixels = ih.get_1d_grayscale(filename)
    w, h = original_image.size

    transformed_pixels = []
    for i in range(len(pixels)):
        col = i % w
        if col % (stripe_width + gap) < stripe_width:
            transformed_pixels.append(0)
        else:
            transformed_pixels.append(pixels[i])

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
        g_new = int(min(g * factor, 255))
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
        tr = int(min(0.393*r + 0.769*g + 0.189*b, 255))
        tg = int(min(0.349*r + 0.686*g + 0.168*b, 255))
        tb = int(min(0.272*r + 0.534*g + 0.131*b, 255))
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
        if number % k == 0:
            return False
    return True


def plot_primes(width, height):
    """Erzeugt ein Schwarz-Weiss-Bild, bei dem Primzahlen schwarze Pixel darstellen."""
    pixels = []
    for i in range(width * height):
        if is_prime(i):
            pixels.append(0)  # Primzahl = schwarz
        else:
            pixels.append(1)  # sonst weiss

    image = ih.generate_bw_image(width, height, pixels)
    image.show()


### ------------------------- ###
### Aufruf aller Funktionen     ###
### ------------------------- ###

# --- Schwarz-Weiss-Bilder ---
bw_file = "ivy_bw.jpg"        # Pfad zum Schwarz-Weiss-Bild
gray_file = "ivy_gray.jpg"    # Pfad zum Graustufen-Bild
rgb_file = "ivy_rgb.jpg"      # Pfad zum RGB-Bild
effi_file = "effi_rgb.jpg"    # Pfad zum RGB-Bild für Sepia

# Aufgabe 1: Anzahl schwarzer Pixel zählen
num_black = count_black_pixels(bw_file)
print(f"Aufgabe 1: Schwarze Pixel in {bw_file}: {num_black}")

# Aufgabe 2: Schwarz-Weiss-Bild invertieren
print("Aufgabe 2: Invertiere Schwarz-Weiss-Bild...")
invert_black_white_image(bw_file)

# Aufgabe 3: Zufälliges Schwarz-Weiss-Bild generieren
print("Aufgabe 3: Zufälliges Schwarz-Weiss-Bild erzeugen...")
random_black_white_image(1000, 600)

# --- Graustufen-Bilder ---
# Aufgabe 4: Graustufen-Bild invertieren
print("Aufgabe 4: Graustufen-Bild invertieren...")
invert_grayscale_image(gray_file)

# Aufgabe 5: Graustufenbild auf 8 Graustufen reduzieren
print("Aufgabe 5: Graustufenbild auf 8 Graustufen reduzieren...")
only_8_shades_of_gray(gray_file)

# Aufgabe 8: Vertikale Streifen hinzufügen
print("Aufgabe 8: Vertikale Streifen hinzufügen...")
vertical_stripes(gray_file)

# --- RGB-Bilder ---
# Aufgabe 6: Grün-Kanal erhöhen
print("Aufgabe 6: Grün-Kanal erhöhen...")
increase_green(rgb_file)

# Aufgabe 7: Sepia-Filter anwenden
print("Aufgabe 7: Sepia-Filter anwenden...")
sepia_filter(effi_file)

# --- Weitere Aufgaben ---
# Aufgabe 9: Primzahlen-Bild erzeugen
print("Aufgabe 9: Primzahlen-Bild erzeugen...")
plot_primes(400, 400)


### ------------------------- ###
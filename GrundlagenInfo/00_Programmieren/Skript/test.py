import subprocess
import turtle

from PIL import Image

# Define file names
EPS_FILE = "turtle_drawing.eps"
SVG_FILE = "turtle_drawing.svg"
PDF_FILE = "turtle_drawing.pdf"


# Create a Turtle drawing
def draw_turtle_graphics():
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(width=100, height=100)
    t.speed(3)

    # Example drawing (modify as needed)
    for _ in range(36):
        t.forward(100)
        t.right(170)

    # Save as EPS
    canvas = screen.getcanvas()
    canvas.postscript(file=EPS_FILE, colormode="color")

    turtle.done()  # Close Turtle


# Convert EPS to SVG using Inkscape
def convert_eps_to_svg():
    try:
        subprocess.run(
            ["inkscape", EPS_FILE, "--export-filename=" + SVG_FILE], check=True
        )
        print(f"✅ Converted to SVG: {SVG_FILE}")
    except FileNotFoundError:
        print("⚠️ Inkscape not found! Please install Inkscape.")


# Convert EPS to PDF using Ghostscript
def convert_eps_to_pdf():
    try:
        image = Image.open(EPS_FILE)
        image.save(PDF_FILE)
        print(f"✅ Converted to PDF: {PDF_FILE}")
    except Exception as e:
        print(f"⚠️ Ghostscript error: {e}")


# Run everything
draw_turtle_graphics()
convert_eps_to_svg()
convert_eps_to_pdf()


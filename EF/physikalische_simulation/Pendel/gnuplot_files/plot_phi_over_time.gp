# Set labels for the axes
set xlabel "time"
set ylabel "angle phi"

# Set title and enable grid
set title "angle over time"
set grid

# Plot the data from the .dat file
plot 't_phi.dat' using 1:2 with lines title 'angle phi'

# Optionally, save the plot as an image file
set terminal pdfcairo enhanced
set output 'angle_over_time.pdf'
replot
set output # Closes the output file

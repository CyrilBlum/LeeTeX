# Set labels for the axes
set xlabel "angle phi"
set ylabel "angular velocity omega"

# Set title and enable grid
set title "phi vs omega"
set grid

# Plot the data from the .dat file
plot 'phi_omega.dat' using 1:2 with lines title 'periodic behaviour'

# Optionally, save the plot as an image file
set terminal pdfcairo enhanced
set output 'phi_vs_omega.pdf'
replot
set output # Closes the output file

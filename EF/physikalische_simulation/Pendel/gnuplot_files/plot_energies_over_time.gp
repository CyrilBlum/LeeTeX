# Set labels for the axes
set xlabel "time"
set ylabel "energy"

# Set title and enable grid
set title "energies over time"
set grid

# Plot the data from the .dat file
plot 'time_energies.dat' using 1:2 with lines title 'kinetic energy', \
     'time_energies.dat' using 1:3 with lines title 'potential energy', \
     'time_energies.dat' using 1:4 with lines title 'total energy'

# Optionally, save the plot as an image file
set terminal pdfcairo enhanced
set output 'energies_over_time.pdf'
replot
set output # Closes the output file

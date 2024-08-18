#!/bin/bash

# Run each Gnuplot script
gnuplot plot_energies_over_time.gp
gnuplot plot_phi_over_time.gp
gnuplot plot_phi_vs_omega.gp 

echo "All Gnuplot scripts have been executed."

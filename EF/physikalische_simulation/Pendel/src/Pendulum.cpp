#include "Pendulum.h"
#include "VelocityVerletSolver.h"
#include <cmath>

Pendulum::Pendulum (double tstart, double tend, unsigned int steps, double v0, double y0, double L, double g, double m)
    : tstart (tstart), tend (tend), steps (steps), v0 (v0), y0 (y0), L (L), g (g), m (m), y (steps + 1), v (steps + 1), time (steps + 1), Ekin (steps + 1), Epot (steps + 1),
      Etot (steps + 1)
{
  evolve_pendulum ();
}

// Variadic template function to handle multiple vectors
template <typename T, typename... Args>
void
Pendulum::write_vectors_to_file (const std::string &filename, const std::vector<T> &vec, const std::vector<Args> &...args) const
{
  // Open the file in write mode
  std::string baseDir = "gnuplot_files/";
  std::ofstream outFile (baseDir + filename);
  // Get the size of the vectors (all vectors are assumed to have the same length)
  std::size_t size = vec.size ();

  // Iterate over the rows
  for (std::size_t i = 0; i < size; ++i)
    {
      // Write each vector's i-th element, followed by a tab
      outFile << vec[i];
      ((outFile << "\t" << args[i]), ...); // Fold expression to write the rest of the vectors
      outFile << std::endl;
    }
}

void
Pendulum::evolve_pendulum ()
{
  // Copy private data members to local variables
  const double g_local = g;
  const double L_local = L;

  VelocityVerletSolver VerletEvolution (tstart, tend, steps, v0, y0, [g_local, L_local] (double y) { return -(g_local / L_local) * std::sin (y); });

  auto [y_verlet, v_verlet, time_verlet] = VerletEvolution.get_all_data ();
  y = y_verlet;
  v = v_verlet;
  time = time_verlet;

  // compute energies
  std::vector<double> Ekin (steps + 1);
  std::vector<double> Epot (steps + 1);
  std::vector<double> Etot (steps + 1);
}

void
Pendulum::compute_energies ()
{
  for (unsigned int k = 0; k < time.size (); ++k)
    {
      Ekin[k] = 0.5 * m * (L * v[k]) * (L * v[k]);
      Epot[k] = m * g * (L - L * std::cos (y[k]));
      Etot[k] = Ekin[k] + Epot[k];
    }
}

void
Pendulum::write_data_to_files () const
{
  // write data to files
  write_vectors_to_file ("phi_omega.dat", y, v);
  write_vectors_to_file ("t_phi.dat", time, y);
  write_vectors_to_file ("t_omega.dat", time, v);
  write_vectors_to_file ("time_energies.dat", time, Ekin, Epot, Etot);
}

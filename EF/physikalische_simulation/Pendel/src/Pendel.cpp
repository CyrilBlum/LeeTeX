#include "Pendel.h"
#include "VelocityVerletSolver.h"

void
write_vectors_to_file (const std::vector<double> &vec1, const std::vector<double> &vec2, const std::string &filename)
{
  // Open the file in write mode
  std::ofstream outFile (filename);
  if (!outFile)
    {
      throw std::ios_base::failure ("Failed to open the file.");
    }
  // Write the vectors to the file
  for (size_t i = 0; i < vec1.size (); ++i)
    {
      outFile << vec1[i] << "\t" << vec2[i] << "\n";
    }

  // Close the file
  outFile.close ();
}

void
write_vectors_to_file (const std::vector<double> &vec1, const std::vector<double> &vec2, const std::vector<double> &vec3, const std::vector<double> &vec4,
                       const std::string &filename)
{
  // Open the file in write mode
  std::ofstream outFile (filename);
  if (!outFile)
    {
      throw std::ios_base::failure ("Failed to open the file.");
    }
  // Write the vectors to the file
  for (size_t i = 0; i < vec1.size (); ++i)
    {
      outFile << vec1[i] << "\t" << vec2[i] << "\t" << vec3[i] << "\t" << vec4[i] << "\n";
    }

  // Close the file
  outFile.close ();
}

void
solve_pendulum (double tstart, double tend, unsigned int steps, double v0, double y0, double L, double g, double m)
{

  VelocityVerletSolver pendulum (tstart, tend, steps, v0, y0, [g, L] (double y) { return -(g / L) * std::sin (y); });
  auto [y, v, time] = pendulum.get_all_data ();

  // compute energies
  std::vector<double> Ekin (steps + 1);
  std::vector<double> Epot (steps + 1);
  std::vector<double> Etot (steps + 1);

  for (unsigned int k = 0; k < time.size (); ++k)
    {
      Ekin[k] = 0.5 * m * (v[k] * v[k]);
      Epot[k] = m * g * (L - L * std::cos (y[k]));
      Etot[k] = Ekin[k] + Epot[k];
    }

  // write data to files
  write_vectors_to_file (y, v, "phi_omega.dat");
  write_vectors_to_file (time, y, "t_phi.dat");
  write_vectors_to_file (time, v, "t_omega.dat");
  write_vectors_to_file (time, Ekin, Epot, Etot, "time_energies.dat");
}

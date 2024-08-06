#include "sv_pendulum.hpp"
#include <string>

void writeVectorToFile(const std::vector<double> &vec0,
                       const std::vector<double> &vec1,
                       const std::string &filename) {
  std::ofstream outFile(filename);

  if (!outFile) {
    std::cerr << "Error opening file: " << filename << std::endl;
    return;
  }

  std::size_t index = 0;
  for (const auto &value : vec0) {
    outFile << value << "\t" << vec1[index] << std::endl;
    ++index;
  }
  outFile.close();
}

int main() {
  typedef double mytype;

  mytype phi0 = 1.570796;
  mytype omega0 = 0.0;
  mytype tspan = 5.0;
  unsigned int n_timesteps = 50000;
  mytype gravity_const = 9.81;
  mytype length = 1.0;
  std::string method = "sv";

  std::vector<mytype> vec_phi_sv(n_timesteps + 1);
  std::vector<mytype> vec_omega_sv(n_timesteps + 1);
  std::vector<mytype> vec_grid(n_timesteps + 1);

  sv_pendulum<mytype>(vec_phi_sv, vec_omega_sv, vec_grid, phi0, omega0, tspan,
                      n_timesteps, gravity_const, length, method);

  // write vector to a file
  std::string filename = "vec.dat";
  writeVectorToFile(vec_grid, vec_phi_sv, filename);

  return 0;
}

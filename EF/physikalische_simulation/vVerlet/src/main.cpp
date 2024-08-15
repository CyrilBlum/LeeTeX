#include "vVerlet.h"
#include <cmath>
void writeVectorsToFile(const std::vector<double> &vec1,
                        const std::vector<double> &vec2,
                        const std::string &filename) {
  // Check if the vectors have the same size
  if (vec1.size() != vec2.size()) {
    throw std::invalid_argument("Vectors must have the same length.");
  }
  // Open the file in write mode
  std::ofstream outFile(filename);
  if (!outFile) {
    throw std::ios_base::failure("Failed to open the file.");
  }
  // Write the vectors to the file
  for (size_t i = 0; i < vec1.size(); ++i) {
    outFile << vec1[i] << "\t" << vec2[i] << "\n";
  }

  // Close the file
  outFile.close();
}

int main() {
  const double g = 9.81;
  const double L = 1;
  vVerlet p(0, 200, 50000, 0, 1.570796,
            [g, L](double y) { return -(g / L) * std::sin(y); });
  auto [y, v, t, Ekin, Epot, Etot] = p.getAllData();

  writeVectorsToFile(t, y, "y_vs_t.dat");
  writeVectorsToFile(y, v, "v_vs_y.dat");
  writeVectorsToFile(t, Etot, "t_vs_Etot.dat");
}

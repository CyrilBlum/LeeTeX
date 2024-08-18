#ifndef Pendel_H_
#define Pendel_H_

#include <fstream>
#include <string>
#include <vector>

class Pendulum
{
public:
  Pendulum (double tstart, double tend, unsigned int steps, double v0, double y0, double L, double g, double m);

  void evolve_pendulum ();

  void compute_energies ();

  void write_data_to_files () const;

private:
  template <typename T, typename... Args> void write_vectors_to_file (const std::string &filename, const std::vector<T> &vec, const std::vector<Args> &...args) const;

  const double tstart;
  const double tend;
  const unsigned int steps;
  const double v0;
  const double y0;
  const double L;
  const double g;
  const double m;

  std::vector<double> y;
  std::vector<double> v;
  std::vector<double> time;
  std::vector<double> Ekin;
  std::vector<double> Epot;
  std::vector<double> Etot;
};

#endif // !Pendel_H_

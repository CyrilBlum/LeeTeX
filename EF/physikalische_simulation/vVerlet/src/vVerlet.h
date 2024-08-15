#ifndef vVERLET_H_
#define vVERLET_H_

#include <array>
#include <cmath>
#include <fstream>
#include <functional>
#include <iostream>
#include <tuple>
#include <vector>

class vVerlet {
public:
  vVerlet(double tstart, double tend, unsigned int steps, double v0, double y0,
          std::function<double(double)> f)
      : tstart(tstart), tend(tend), steps(steps), y(steps + 1), v(steps + 1),
        t(steps + 1), Ekin(steps + 1), Epot(steps + 1), Etot(steps + 1), f(f) {

    // initialize uniform time grid
    for (unsigned int k = 0; k < t.size(); ++k) {
      t[k] = h * k;
    }

    // set initial values v0 and y0
    v[0] = v0;
    y[0] = y0;

    verlet_solve();
    compute_energies();
  }

  std::tuple<std::vector<double>, std::vector<double>, std::vector<double>,
             std::vector<double>, std::vector<double>, std::vector<double>>
  getAllData() const {
    return std::make_tuple(y, v, t, Ekin, Epot, Etot);
  }

private:
  const double tstart;
  const double tend;
  const unsigned int steps;
  const double h = (tend - tstart) / steps;

  std::vector<double> y;
  std::vector<double> v;
  std::vector<double> t;
  std::vector<double> Ekin;
  std::vector<double> Epot;
  std::vector<double> Etot;
  std::function<double(double)> f;

  void single_verlet_step(unsigned int k) {
    // step 1: compute y_{k+1}
    y[k + 1] = y[k] + h * v[k] + h * h * f(y[k]) / 2.0;
    // step 2: compute v_{k+1}
    v[k + 1] = v[k] + h / (2.0) * (f(y[k]) + f(y[k + 1]));
  }

  void verlet_solve() {
    for (unsigned int k = 0; k < steps; ++k) {
      single_verlet_step(k);
    }
  }

  void compute_energies() {
    for (unsigned int k = 0; k < t.size(); ++k) {
      Ekin[k] = 0.5 * (v[k] * v[k]);
      Epot[k] = -9.81 * std::cos(y[k]);
      Etot[k] = Ekin[k] + Epot[k];
    }
  }
};

#endif // !vVERLET_H_

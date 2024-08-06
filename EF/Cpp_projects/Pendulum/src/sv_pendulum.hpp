#pragma once

#include <cmath>
#include <fstream>
#include <iostream>
#include <ostream>
#include <string>
#include <vector>
template <typename T>
void sv_pendulum(std::vector<T> &vec_phi_sv, std::vector<T> &vec_omega_sv,
                 std::vector<T> &vec_grid, T phi0, T omega0, T tspan,
                 unsigned int n_timesteps, T gravity_const, T length,
                 std::string method) {

  T h = tspan / n_timesteps;

  auto f = [](T phi, T gravity_const, T length) {
    return -gravity_const * sin(phi) / length;
  };

  if (method == "sv") {
    // initial step
    auto phi_old = phi0;
    auto phi_new =
        h * omega0 + phi0 + 0.5 * h * h * f(phi0, gravity_const, length);

    // Stoermer-Verlet iteration
    vec_phi_sv[0] = phi0;
    vec_phi_sv[1] = phi_new;

    vec_omega_sv[0] = omega0;

    vec_grid[0] = 0.0;

    T phi;
    auto two_h = 2 * h;

    for (unsigned int k = 1; k <= n_timesteps; ++k) {
      phi =
          -phi_old + 2.0 * phi_new + h * h * f(phi_new, gravity_const, length);
      vec_omega_sv[k] = (phi - phi_old) / two_h;
      phi_old = phi_new;
      phi_new = phi;
      vec_phi_sv[k] = phi;

      vec_grid[k] = vec_grid[k - 1] + h;
    }
  }
}

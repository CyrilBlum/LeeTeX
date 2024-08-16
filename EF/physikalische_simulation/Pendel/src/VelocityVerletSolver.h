#ifndef VelocityVerletSolver_H_
#define VelocityVerletSolver_H_

#include <cmath>
#include <functional>
#include <tuple>
#include <vector>

class VelocityVerletSolver
{
public:
  VelocityVerletSolver (double tstart, double tend, unsigned int steps, double v0, double y0, std::function<double (double)> f);

  std::tuple<std::vector<double>, std::vector<double>, std::vector<double> > get_all_data () const;

private:
  const double tstart;
  const double tend;
  unsigned int current_step = 0;            // current step
  const unsigned int steps;                 // number of steps
  const double h = (tend - tstart) / steps; // step size

  std::vector<double> y;
  std::vector<double> v;
  std::vector<double> time;
  std::function<double (double)> f;

  void single_velocity_verlet_step ();
  void solve ();
};

#endif // !VelocityVerletSolver_H_

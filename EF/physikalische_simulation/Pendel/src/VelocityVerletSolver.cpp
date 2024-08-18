#include "VelocityVerletSolver.h"

VelocityVerletSolver::VelocityVerletSolver (double tstart, double tend, unsigned int steps, double v0, double y0, std::function<double (double)> f)
    : tstart (tstart), tend (tend), steps (steps), y (steps + 1), v (steps + 1), time (steps + 1), f (f)
{
  // compute (uniform) time grid
  for (unsigned int k = 0; k < time.size (); ++k)
    {
      time[k] = h * k + tstart;
    }

  // set initial values of y and v
  y[0] = y0;
  v[0] = v0;

  // compute the velocity verlet evolution
  solve ();
}

std::tuple<std::vector<double>, std::vector<double>, std::vector<double> >
VelocityVerletSolver::get_all_data () const
{
  return std::make_tuple (y, v, time);
}

void
VelocityVerletSolver::single_velocity_verlet_step ()
{
  // step 1: compute y_{k+1}
  y[current_step + 1] = y[current_step] + h * v[current_step] + h * h * f (y[current_step]) / 2.0;
  // step 2: compute v_{k+1}
  v[current_step + 1] = v[current_step] + h / (2.0) * (f (y[current_step]) + f (y[current_step + 1]));
  ++current_step;
}

void
VelocityVerletSolver::solve ()
{
  for (unsigned int k = 0; k < steps; ++k)
    {
      single_velocity_verlet_step ();
    }
}

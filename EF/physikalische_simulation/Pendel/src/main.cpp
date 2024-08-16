#include "Pendel.h"

int
main ()
{
  const double tstart = 0.0;
  const double tend = 5.0;
  const unsigned int steps = 600;

  const double v0 = 0.0;
  const double y0 = 1.570796;
  const double g = 9.81;
  const double L = 1;
  const double m = 1;
  solve_pendulum (tstart, tend, steps, v0, y0, L, g, m);
}

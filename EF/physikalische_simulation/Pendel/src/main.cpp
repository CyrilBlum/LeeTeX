#include "Pendulum.h"

int
main ()
{
  const double tstart = 0;
  const double tend = 10.0;
  const unsigned int steps = 5000;

  const double v0 = 0.0;
  const double y0 = 1.570796;
  const double g = 9.81;
  const double L = 1;
  const double m = 1;

  Pendulum p (tstart, tend, steps, v0, y0, L, g, m);
  p.compute_energies ();
  p.write_data_to_files ();
}

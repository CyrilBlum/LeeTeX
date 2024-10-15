#include <eigen3/Eigen/Dense>
#include "matplotlibcpp.h"
namespace plt = matplotlibcpp;

int main() {
  int n = 5000;
  Eigen::VectorXd x(n), y(n), z(n), w = Eigen::VectorXd::Ones(n);
  for (int i = 0; i < n; ++i) {
    double value = (1.0 + i) / n;
    x(i) = value;
    y(i) = value * value;
    z(i) = value * value * value;
  }

  plt::loglog(x, y);         // f(x) = x^2
  plt::loglog(x, w, "r--");  // f(x) = 1, red dashed line
  plt::loglog(x, z,
              "g:", {{"label", "$x^3$"}});  // f(x) = x^3, green dots + label

  plt::title("Some functions of $x$");  // add a title
  plt::show();
}

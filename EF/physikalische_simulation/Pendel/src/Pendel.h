#ifndef Pendel_H_
#define Pendel_H_

#include <fstream>
#include <string>
#include <vector>
void write_vectors_to_file (const std::vector<double> &vec1, const std::vector<double> &vec2, const std::string &filename);

void write_vectors_to_file (const std::vector<double> &vec1, const std::vector<double> &vec2, const std::vector<double> &vec3, const std::string &filename);

void solve_pendulum (double tstart, double tend, unsigned int steps, double v0, double y0, double L, double g, double m);
#endif // !Pendel_H_

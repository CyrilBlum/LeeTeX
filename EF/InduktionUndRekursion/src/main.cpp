#include "n_queen_problem.h"
#include <iostream>
int main() {
    Queen_Problem Q = Queen_Problem(8);
    Q.solve_queen_problem();
    std::cout << Q.get_number_of_solutions() << std::endl;
    return 0;
}

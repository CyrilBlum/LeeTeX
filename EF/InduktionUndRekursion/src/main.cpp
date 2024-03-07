// main.cpp
#include <iostream>
#include "n_queen_problem.h"

int main()
{
	for (unsigned int n = 8; n <= 8; ++n)
	{
		Queen_Problem p(n);
		p.solve_queen_problem();
		std::cout << n << ": " << p.get_number_of_solutions() << "\n";
	}
	return 0;
}

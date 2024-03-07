// n_queen_problem.cpp

#include <iostream>
#include <cstring>
#include "n_queen_problem.h"

Queen_Problem::Queen_Problem(const unsigned int board_size) : number_of_solutions{0}, n{board_size}
{
	board = new bool*[n];
	for (unsigned int i = 0; i < n; ++i)
	{
		board[i] = new bool[n];
		memset(board[i], false, n * sizeof(bool));
	}
}

void Queen_Problem::print_solution(void) const
{
	std::cout << "\n";
	for (unsigned int i = 0; i < n; ++i)
	{
		for (unsigned int j = 0; j < n; ++j)
		{
			std::cout << board[i][j] << " ";
		}
		std::cout << "\n";
	}
	std::cout << "\n";
}

bool Queen_Problem::check_square(const unsigned int row, const unsigned int column) const
{
	int i;
	int j;

	// check if column is already occupied by a queen in one of the rows above
	for (i = row - 1; i >= 0; --i)
	{
		if (board[i][column] == 1)
		{
			return false;
		}
	}

	// check north-western diagonal
	for (i = row - 1, j = column - 1; (i >= 0) and (j >= 0); --i, --j)
	{
		if (board[i][j] == 1)
		{
			return false;
		}
	}

	// check north-eastern diagonal
	for (i = row - 1, j = column + 1; (i >= 0) and (j < static_cast<int>(n)); --i, ++j)
	{
		if (board[i][j] == 1)
		{
			return false;
		}
	}
	return true;
}

void Queen_Problem::solve_queen_problem(const unsigned int row)
{
	if (row == n)
	{
		print_solution();
		++number_of_solutions;
		return;
	}

	for (unsigned int j = 0; j < n; ++j)
	{
		if ( check_square(row, j) )
		{
			board[row][j] = 1;
			solve_queen_problem(row + 1);
			board[row][j] = 0;
		}
	}
}

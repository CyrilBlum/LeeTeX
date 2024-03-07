// n_queen_problem.h

class Queen_Problem
{
	public:
		Queen_Problem(const unsigned int);
		~Queen_Problem(void)
		{
			for (unsigned int i = 0; i < n; ++i)
			{
				delete[] board[i];
			}
			delete[] board;
		}
		void print_solution(void) const;
		bool check_square(const unsigned int, const unsigned int) const;
		void solve_queen_problem(const unsigned int = 0);
		unsigned long long get_number_of_solutions(void) const
		{
			return number_of_solutions;
		}

	private:
		unsigned long long number_of_solutions;
		unsigned int n;
		bool** board;
};

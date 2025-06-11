# def print_move(start,end):
# 	print(start, "-->", end)

# def hanoi(n, start, end):
# 	cstart = start
# 	cend = end
# 	print('hanoi(',n,',',start,',',end,')',sep='')
# 	if n == 1:
# 		print_move(cstart,cend)
# 		# print('print_move(',cstart,',',cend,')',sep='')
# 	else:
# 		other = 6 - (start + end)
# 		cother = other
# 		end = other

# 		hanoi(n - 1, start, end)
# 		print_move(cstart, cend)
# 		# print('print_move(',cstart,',',cend,')',sep='')
# 		start = cother
# 		end = cend
# 		hanoi(n-1, start, end)

# hanoi(3, 1, 3)



def print_move(start, end):
	print(start, "-->", end)

def hanoi(n, start, end):
	if n == 1:
		print_move(start, end)
	else:
		other = 6 - (start + end)
		hanoi(n - 1, start, other)
		print_move(start, end)
		hanoi(n-1, other, end)

hanoi(3, 1, 2)
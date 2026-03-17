n = 8
s = 3
upper_left = 'white'

black_white = int(n/2) * (s * '1' + s * '0')
white_black = int(n/2) * (s * '0' + s * '1')

if upper_left == 'black':
    first = black_white
    second = white_black
else:
    first = white_black
    second = black_white

for _ in range(int(n/2)):
    for _ in range(s):
        print(first)
    for _ in range(s):
        print(second)
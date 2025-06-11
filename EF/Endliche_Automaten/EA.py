import random


def EA0(w, start):
    q = start
    accepting = ["q2", "q3"]

    for char in w:
        if q == "q0":
            if char == "0":
                q = "q0"
            elif char == "1":
                q = "q1"
        elif q == "q1":
            if char == "0":
                q = "q2"
            elif char == "1":
                q = "q3"
        elif q == "q2":
            if char == "0":
                q = "q0"
            elif char == "1":
                q = "q1"
        elif q == "q3":
            if char == "0":
                q = "q2"
            elif char == "1":
                q = "q3"

    return q in accepting


def EA1(w, start):
    q = start
    accepting = ["q2", "q4"]

    for char in w:
        if q == "q0":
            if char == "0":
                q = "q3"
            elif char == "1":
                q = "q1"
        elif q == "q1":
            if char == "0":
                q = "q4"
            elif char == "1":
                q = "q2"
        elif q == "q2":
            if char == "0":
                q = "q4"
            elif char == "1":
                q = "q2"
        elif q == "q3":
            if char == "0":
                q = "q3"
            elif char == "1":
                q = "q1"
        elif q == "q4":
            if char == "0":
                q = "q3"
            elif char == "1":
                q = "q1"
    return q in accepting


def generate_binary_string(n):
    # Generate a random number with n bits
    number = random.getrandbits(n)
    # Convert the number to binary
    binary_string = format(number, "0b")
    return binary_string


def compare(number, lmax):
    for _ in range(0, number):
        n = random.randint(0, lmax)
        word = generate_binary_string(n)
        if EA0(word, "q0") != EA1(word, "q0"):
            print("OHHHHHHH NOOOOOOOO!!!!!!!")
            return False
    return True


print(compare(5000, 10))

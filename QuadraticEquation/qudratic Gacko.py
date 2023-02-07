def parse_input():
    pass


def get_a(a):
    pass


def get_b(a):
    pass


def get_c(a):
    pass


def solve_d(a, b, ca):
    pass


math_problems = ["-0.5X2-5X-18=0", "2X2+5X+18=0", "2X2+5X-18=0"]
for math_problem in math_problems:
    print(math_problem)
    equation = math_problem.split("X")

    a = float(equation[0])
    if "+" in equation[1]:
        b = float(equation[1].split("+")[1])
    elif "-" in equation[1]:
        b = float(equation[1].split("-")[1]) * -1
    c = float(equation[2].split("=")[0])

    d = b ** 2 - 4 * a * c
    if d > 0:
        print((-b + d ** 0.5) / (2 * a))
        print((-b - d ** 0.5) / (2 * a))
    elif d == 0:
        print(-b / (2 * a))
    else:
        print("No solutions")

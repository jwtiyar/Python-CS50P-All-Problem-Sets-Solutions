def math():
    formula = input("Expression: ")
    x, y, z = formula.split(" ")
    if y == "+":
        answer = int(x) + int(z)
        # print(answer)
    elif y == "/":
        answer = int(x) / int(z)
    elif y == "-":
        answer = int(x) - int(z)
    elif y == "*":
        answer = int(x) * int(z)
    answer = f'{answer:.1f}'
    return answer

print(math())

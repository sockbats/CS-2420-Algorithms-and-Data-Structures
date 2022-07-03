from stack import Stack


def in2post(expr):
    if expr is None:
        raise ValueError
    expr = expr.replace(" ", "")
    my_stack = Stack()
    output = ""
    for i in expr:
        if i in "+-*/(":
            if my_stack.size() <= 0:
                my_stack.push(i)
            elif i in "*/":
                my_stack.push(i)
            elif i in "+-":
                if my_stack.top() in "*/":
                    while my_stack.size() > 0 and my_stack.top() != "(":
                        output += my_stack.pop()
                elif my_stack.top() in "+-":
                    output += my_stack.pop()
                my_stack.push(i)
            else:
                my_stack.push(i)
        elif i == ")":
            while my_stack.size() > 0 and my_stack.top() != "(":
                if my_stack.size() == 1 and my_stack.top() != "(":
                    raise SyntaxError
                output += my_stack.pop()
            if my_stack.top() == "(":
                my_stack.pop()
        else:
            output += i
    while my_stack.size() > 0:
        output += my_stack.pop()
    return output


def eval_postfix(expr):
    if expr is None:
        raise ValueError
    expr = expr.replace(" ", "")
    my_list = list(expr)
    if len(my_list) < 3:
        return float(expr)
    i = 0
    try:
        while i < len(my_list):
            if my_list[i] in "+-*/":
                my_list[i-2] = eval(f"{my_list[i-2]}{my_list[i]}{my_list[i-1]}")
                my_list.pop(i)
                my_list.pop(i-1)
                i -= 2
            i += 1
        return float(my_list[0])
    except IndexError:
        raise SyntaxError


def main():
    with open("data.txt", "r") as f:
        data = [x.strip() for x in f.read().strip().split("\n")]
    for i in data:
        print("Infix:", i)
        post = in2post(i)
        print("Postfix:", post)
        print("Answer:", eval_postfix(post), "\n")


if __name__ == '__main__':
    main()

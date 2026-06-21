def precedence(op):
    if op in ("+", "-"):
        return 1
    if op in ("*", "/"):
        return 2
    return 0


def apply_op(a, b, op):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


def evaluate(expression):
    values = []
    ops = []

    i = 0
    n = len(expression)

    while i < n:
        if expression[i] == " ":
            i += 1
            continue

        # number (supports decimals)
        if expression[i].isdigit() or expression[i] == ".":
            num = ""
            dot_count = 0

            while i < n and (expression[i].isdigit() or expression[i] == "."):
                if expression[i] == ".":
                    dot_count += 1
                    if dot_count > 1:
                        raise ValueError("Invalid number format")
                num += expression[i]
                i += 1

            values.append(float(num))
            continue

        # operator check
        if expression[i] in "+-*/":
            while ops and precedence(ops[-1]) >= precedence(expression[i]):
                b = values.pop()
                a = values.pop()
                op = ops.pop()
                values.append(apply_op(a, b, op))

            ops.append(expression[i])
            i += 1
        else:
            raise ValueError(f"Invalid character: {expression[i]}")

    while ops:
        b = values.pop()
        a = values.pop()
        op = ops.pop()
        values.append(apply_op(a, b, op))

    return values[0]


# 🔁 Main loop (never breaks unless you quit)
while True:
    expr = input("Enter expression (or q to quit): ")

    if expr.lower() == "q":
        print("Goodbye!")
        break

    try:
        result =  (expr)
        print("Result:", result)

    except ZeroDivisionError as e:
        print("Math error:", e)

    except Exception as e:
        print("Invalid input:", e)
    
    
    
    
    
    
    
    
    
    
           
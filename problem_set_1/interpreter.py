def main():
    expression = input("What math would you like to do? ")
    print(interpret(expression))

def interpret(input):
    x, y, z = input.split(" ")

    x = float(x)
    z = float(z)

    match y:
        case '+':
            return x + z
        case '-':
            return x  - z
        case '*':
            return x * z
        case '/':
            return x / z
        case _:
            return "Not a proper expression, try again"

main()

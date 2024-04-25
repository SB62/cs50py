def main():
    mass = input("Input the mass of the object you want to calculate the amount of energy (in Joules) for: ")
    print(einstein(mass))

def einstein(mass):
    speedoflight = 300000000
    return int(mass) * pow(speedoflight, 2)

main()

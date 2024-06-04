def main():
    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
        if coin in {5, 10, 25}:
            amount_due -= coin
        else:
            print("Enter correct change only please!")

        if amount_due <= 0:
            change = abs(amount_due)
            print(f"Change Owed: {change}")

if __name__ == "__main__":
    main()

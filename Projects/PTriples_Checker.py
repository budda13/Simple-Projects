while True:
    a = int(input("Enter side one."))
    b = int(input("Enter side two."))
    c = int(input("Enter side three."))

    if (a**2 + b**2 == c**2) or (c**2 + b**2 == a**2) or (a**2 + c**2 == b**2):
        print("This is a Pythagorean Triple!")
    else:
        print("This is not a Pythagorean Triple.")

    q = input("Check again? (Y/N)")
    if q == 'n' or q == 'N':
        print("if statement runs")
        break

pass

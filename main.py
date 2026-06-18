def km_to_m(km):
    return km * 1000

def m_to_km(m):
    return m / 1000

def kg_to_g(kg):
    return kg * 1000

def g_to_kg(g):
    return g / 1000

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

while True:
    print("\n===== UNIT CONVERTER TOOL =====")
    print("1. Kilometer to Meter")
    print("2. Meter to Kilometer")
    print("3. Kilogram to Gram")
    print("4. Gram to Kilogram")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        km = float(input("Enter Kilometer: "))
        print("Meters =", km_to_m(km))

    elif choice == "2":
        m = float(input("Enter Meter: "))
        print("Kilometers =", m_to_km(m))

    elif choice == "3":
        kg = float(input("Enter Kilogram: "))
        print("Grams =", kg_to_g(kg))

    elif choice == "4":
        g = float(input("Enter Gram: "))
        print("Kilograms =", g_to_kg(g))

    elif choice == "5":
        c = float(input("Enter Celsius: "))
        print("Fahrenheit =", c_to_f(c))

    elif choice == "6":
        f = float(input("Enter Fahrenheit: "))
        print("Celsius =", round(f_to_c(f), 2))

    elif choice == "7":
        print("Thank you for using Unit Converter!")
        break

    else:
        print("Invalid Choice. Try Again.")
import sys

print(r"""
_ __                                     __
__  ______  (_) /_   _________  ____ _   _____  _____/ /_____  _____
/ / / / __ \/ / __/  / ___/ __ \/ __ \ | / / _ \/ ___/ __/ __ \/ ___/
/ /_/ / / / / / /_   / /__/ /_/ / / / / |/ /  __/ /  / /_/ /_/ / /
\__,_/_/ /_/_/\__/   \___/\____/_/ /_/|___/\___/_/   \__/\____/_/
""")

print("=" * 116)

print(r"""

[A] Metrics          [B] Weight          [C] Temperature

[D] Data             [E] Time            [F] Speed

[G] Area             [H] Volume          [Q] Exit

""")

choix = input("Select category:... ")

if choix.lower() == "q":
    print(r"""

______  ________   ______  ________
/ __ ) \/ / ____/  / __ ) \/ / ____/
/ __  |\  / __/    / __  |\  / __/
/ /_/ / / / /___   / /_/ / / / /___
/_____/ /_/_____/  /_____/ /_/_____/

""")
    sys.exit()

elif choix.lower() == "a":

    print(r"""

1) Kilometer  to  Mile
2) Mile       to  Kilometer
3) Meter      to  Feet
4) Feet       to  Meter

""")

    choix2 = int(input())

    if choix2 == 1:
        mesure = float(input("Enter a measurement:..."))
        print("km:", mesure, "mile:", 0.621371 * mesure)

    elif choix2 == 2:
        mesure = float(input("Enter a measurement:..."))
        print("mile:", mesure, "km:", mesure / 0.621371)

    elif choix2 == 3:
        mesure = float(input("Enter a measurement:..."))
        print("meter:", mesure, "feet:", mesure * 3.28084)

    elif choix2 == 4:
        mesure = float(input("Enter a measurement:..."))
        print("feet:", mesure, "meter:", mesure / 3.28084)

    else:
        sys.exit()


elif choix.lower() == "b":

    print(r"""

1) Kilogram  to  Pound
2) Pound     to  Kilogram
3) Gram      to  Ounce
4) Ounce     to  Gram
5) Kilogram  to  Gram
6) Gram      to  Kilogram

""")

    choix2 = int(input())

    if choix2 == 1:
        weight = float(input("Enter the weight:..."))
        print("KG:", weight, "Pound:", 2.20462 * weight)

    elif choix2 == 2:
        weight = float(input("Enter the weight:..."))
        print("Pound:", weight, "KG:", weight / 2.20462)

    elif choix2 == 3:
        weight = float(input("Enter the weight:..."))
        print("Gram:", weight, "Ounce:", weight * 0.035274)

    elif choix2 == 4:
        weight = float(input("Enter the weight:..."))
        print("Ounce:", weight, "Gram:", weight / 0.035274)

    elif choix2 == 5:
        weight = float(input("Enter the weight:..."))
        print("KG:", weight, "Gram:", weight * 1000)

    elif choix2 == 6:
        weight = float(input("Enter the weight:..."))
        print("Gram:", weight, "KG:", weight / 1000)


elif choix.lower() == "c":

    print(r"""

1) Celsius     to  Fahrenheit
2) Fahrenheit  to  Celsius
3) Celsius     to  Kelvin
4) Kelvin      to  Celsius
5) Fahrenheit  to  Kelvin
6) Kelvin      to  Fahrenheit

""")

    choix2 = int(input())
    temp = 0.0

    if choix2 == 1:
        temp = float(input("Enter Temperature... "))
        print("Celsius:", temp, "Fahrenheit:", (temp * 9 / 5) + 32)

    elif choix2 == 2:
        temp = float(input("Enter Temperature... "))
        print("Fahrenheit:", temp, "Celsius:", (temp - 32) * 5 / 9)

    elif choix2 == 3:
        temp = float(input("Enter Temperature... "))
        print("Celsius:", temp, "Kelvin:", temp + 273.15)

    elif choix2 == 4:
        temp = float(input("Enter Temperature... "))
        print("Kelvin:", temp, "Celsius:", temp - 273.15)

    elif choix2 == 5:
        temp = float(input("Enter Temperature... "))
        print("Fahrenheit:", temp, "Kelvin:", (temp - 32) * 5 / 9 + 273.15)

    elif choix2 == 6:
        temp = float(input("Enter Temperature... "))
        print("Kelvin:", temp, "Fahrenheit:", (temp - 273.15) * 9 / 5 + 32)


elif choix.lower() == "d":

    print(r"""

1) Byte       to  Kilobyte
2) Kilobyte   to  Byte
3) Megabyte   to  Gigabyte
4) Gigabyte   to  Megabyte
5) Megabyte   to  Byte
6) Byte       to  Megabyte

""")

    choix2 = int(input())
    data = 0

    if choix2 == 1:
        data = float(input("Enter data:..."))
        print("Byte:", data, "KB:", data / 1024)

    elif choix2 == 2:
        data = float(input("Enter data:..."))
        print("KB:", data, "Byte:", data * 1024)

    elif choix2 == 3:
        data = float(input("Enter data:..."))
        print("MB:", data, "GB:", data / 1024)

    elif choix2 == 4:
        data = float(input("Enter data:..."))
        print("GB:", data, "MB:", data * 1024)

    elif choix2 == 5:
        data = float(input("Enter data:..."))
        print("MB:", data, "Byte:", data * 1024 * 1024)

    elif choix2 == 6:
        data = float(input("Enter data:..."))
        print("Byte:", data, "MB:", data / (1024 * 1024))


elif choix.lower() == "e":

    print(r"""

1) Seconds  to  Minutes
2) Minutes  to  Seconds
3) Minutes  to  Hours
4) Hours    to  Minutes
5) Hours    to  Seconds
6) Seconds  to  Hours

""")

    choix2 = int(input())
    time = 0

    if choix2 == 1:
        time = float(input("Enter time:..."))
        print("Seconds:", time, "Minutes:", time / 60)

    elif choix2 == 2:
        time = float(input("Enter time:..."))
        print("Minutes:", time, "Seconds:", time * 60)

    elif choix2 == 3:
        time = float(input("Enter time:..."))
        print("Minutes:", time, "Hours:", time / 60)

    elif choix2 == 4:
        time = float(input("Enter time:..."))
        print("Hours:", time, "Minutes:", time * 60)

    elif choix2 == 5:
        time = float(input("Enter time:..."))
        print("Hours:", time, "Seconds:", time * 3600)

    elif choix2 == 6:
        time = float(input("Enter time:..."))
        print("Seconds:", time, "Hours:", time / 3600)


elif choix.lower() == "f":

    print(r"""

1) Kilometer/hour  to  Mile/hour
2) Mile/hour       to  Kilometer/hour
3) Meter/second    to  Kilometer/hour
4) Kilometer/hour  to  Meter/second

""")

    choix2 = int(input())
    speed = 0

    if choix2 == 1:
        speed = float(input("Enter speed:..."))
        print("Km/h:", speed, "Mile/h:", speed * 0.621371)

    elif choix2 == 2:
        speed = float(input("Enter speed:..."))
        print("Mile/h:", speed, "Km/h:", speed / 0.621371)

    elif choix2 == 3:
        speed = float(input("Enter speed:..."))
        print("m/s:", speed, "Km/h:", speed * 3.6)

    elif choix2 == 4:
        speed = float(input("Enter speed:..."))
        print("Km/h:", speed, "m/s:", speed / 3.6)


elif choix.lower() == "g":

    print(r"""

1) Square Meter      to  Square Foot
2) Square Foot       to  Square Meter
3) Square Kilometer  to  Square Mile
4) Square Mile       to  Square Kilometer

""")

    choix2 = int(input())
    area = 0

    if choix2 == 1:
        area = float(input("Enter area:..."))
        print("m²:", area, "ft²:", area * 10.7639)

    elif choix2 == 2:
        area = float(input("Enter area:..."))
        print("ft²:", area, "m²:", area / 10.7639)

    elif choix2 == 3:
        area = float(input("Enter area:..."))
        print("km²:", area, "mile²:", area * 0.386102)

    elif choix2 == 4:
        area = float(input("Enter area:..."))
        print("mile²:", area, "km²:", area / 0.386102)


elif choix.lower() == "h":

    print(r"""

1) Liter       to  Gallon
2) Gallon      to  Liter
3) Liter       to  Milliliter
4) Milliliter  to  Liter
5) Cubic Meter to  Liter
6) Liter       to  Cubic Meter

""")

    choix2 = int(input())
    volume = 0

    if choix2 == 1:
        volume = float(input("Enter volume:..."))
        print("Liter:", volume, "Gallon:", volume * 0.264172)

    elif choix2 == 2:
        volume = float(input("Enter volume:..."))
        print("Gallon:", volume, "Liter:", volume / 0.264172)

    elif choix2 == 3:
        volume = float(input("Enter volume:..."))
        print("Liter:", volume, "Milliliter:", volume * 1000)

    elif choix2 == 4:
        volume = float(input("Enter volume:..."))
        print("Milliliter:", volume, "Liter:", volume / 1000)

    elif choix2 == 5:
        volume = float(input("Enter volume:..."))
        print("m³:", volume, "Liter:", volume * 1000)

    elif choix2 == 6:
        volume = float(input("Enter volume:..."))
        print("Liter:", volume, "m³:", volume / 1000)

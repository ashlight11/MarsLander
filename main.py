# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import scipy
from scipy import integrate


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def simulation():
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point.
    # By linking all the points together in a sequential fashion, you form the surface of Mars.
    number_points = 6
    ground = [(0, 1500), (1000, 2000), (2000, 500), (3500, 500), (5000, 1500), (6999, 1000)]
    # hs: the horizontal speed (in m/s), can be negative.
    # vs: the vertical speed (in m/s), can be negative.
    # f: the quantity of remaining fuel in liters.
    # r: the rotation angle in degrees (-90 to 90).
    # p: the thrust power (0 to 4).
    input_first = "5000 2500 -50 0 1000 90 0"  # (X Y hSpeed vSpeed fuel rotate power)
    output_values = "-45 4"
    input_second = "4950 2498 -51 -3 999 75 1"
    input_third = "4898 2493 -53 -6 997 60 2"

    begin_flat, end_flat = find_landing_area(ground)

    x, y, hs, vs, f, r, p = [int(i) for i in input_second.split()]
    rotate, power = [int(i) for i in output_values.split()]
    print(x, y, hs, vs, f, r, p)
    print(rotate, power)
    g = -3.711
    new_power = p + power if power <= 1 else p + 1
    new_r = r + rotate if abs(rotate) < 15 else r + math.copysign(15, rotate)

    new_vs = vs + (g + new_power) * math.sin(new_r * math.pi / 180)
    # new_vs = vs + g + new_power

    new_hs = hs + new_vs * math.cos(new_r * math.pi / 180)

    new_x = x + new_hs
    new_y = y + new_vs
    new_fuel = f - new_power

    print(new_x, new_y, new_hs, new_vs, new_fuel, new_r, new_power)

    new_vs = round(new_vs)
    new_hs = round(new_hs)
    new_r = round(new_r)

    new_x = round(x + new_hs)
    new_y = round(y + new_vs)

    print(new_x, new_y, new_hs, new_vs, new_fuel, new_r, new_power)


def find_landing_area(ground):
    begin_flat = 0
    end_flat = 0
    for index, element in enumerate(ground):
        if index != len(ground) - 1 and element[1] == ground[index + 1][1]:
            begin_flat = element
            end_flat = ground[index + 1]

    return begin_flat, end_flat


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    simulation()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

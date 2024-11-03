try:
    rhombus1 = rhombus(10, 60)
    print(rhombus1)
except Exception as e:
    print("Test failed:", e)

try:
    rhombus2 = rhombus(15, 45)
    print(rhombus2)
except Exception as e:
    print("Test failed:", e)

try:
    rhombus(0, 60)
except ValueError as e:
    print("Test passed for invalid side length:", e)

try:
    rhombus(10, 180)
except ValueError as e:
    print("Test passed for invalid angle кут_а >= 180:", e)

try:
    rhombus(10, -10)
except ValueError as e:
    print("Test passed for invalid angle angle_а <= 0:", e)

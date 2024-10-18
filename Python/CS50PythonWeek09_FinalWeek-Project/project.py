import math

def main():
    while True:
        try:
            base = BaseOfTriangle()
            opposite = OppositeOfTriangle()
            hypotenuse = HypotenuseOfTriangle(base, opposite)
            calculations = calculation_logic(base, opposite, hypotenuse)
            printer(calculations)
        except Exception as e:
            print(f"An error occurred: {e}")

def BaseOfTriangle():
    return float(input("Enter the base of the triangle: "))

def OppositeOfTriangle():
    return float(input("Enter the opposite side of the triangle: "))

def HypotenuseOfTriangle(base, opposite):
    return math.sqrt(base**2 + opposite**2)

def calculation_logic(base, opposite, hypotenuse):
    sin = opposite / hypotenuse
    cos = base / hypotenuse
    tan = opposite / base
    sec = 1 / cos
    cosec = 1 / sin
    cot = 1 / tan
    return {'sin': sin, 'cos': cos, 'tan': tan, 'sec': sec, 'cosec': cosec, 'cot': cot}

def printer(calculations):
    for k, v in calculations.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()

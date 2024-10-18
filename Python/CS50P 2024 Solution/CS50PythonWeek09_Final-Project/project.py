import math
import matplotlib.pyplot as plt
from PIL import Image


def main():
    while True:
        try:
            base = float(input("Enter the base of the triangle: "))
            opposite = float(input("Enter the opposite side of the triangle: "))

            hypotenuse = HypotenuseOfTriangle(base, opposite)
            results = calculation_logic(base, opposite, hypotenuse)
            printer(results)
            generate_image(base, opposite, hypotenuse, results)
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\nProgram terminated.")
            break


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

    return {"sin": sin, "cos": cos, "tan": tan, "sec": sec, "cosec": cosec, "cot": cot}


def printer(results):
    print("\nTrigonometric Ratios:")
    for key, value in results.items():
        print(f"{key}: {value:.4f}")

def generate_image(base, opposite, hypotenuse, results):
    fig, ax = plt.subplots()

    # Draw the triangle
    triangle = plt.Polygon(((0, 0), (base, 0), (0, opposite)), fill=None, edgecolor='black')
    ax.add_patch(triangle)

    # Annotate the sides
    ax.text(base / 2, -0.05 * opposite, f"Base = {base}", ha='center')
    ax.text(-0.01 * base, opposite / 2, f"Height = {opposite}", va='center', rotation='vertical')
    ax.text(base / 1.9, opposite / 2.2, f"Hypotenuse = {round(hypotenuse, 2)}", rotation=-45)

    # Add the table of trigonometric values
    table_data = [[key, f"{value:.4f}"] for key, value in results.items()]
    table = plt.table(cellText=table_data,
                      colLabels=["Function", "Value"],
                      cellLoc="center",
                      loc="right",
                      colColours=["#f2f2f2", "#f2f2f2"])
    table.scale(1, 2)

    # Set limits and aspect ratio
    ax.set_xlim(0, base + 1)
    ax.set_ylim(0, opposite + 1)
    ax.set_aspect('equal')

    plt.axis('off')

    # Save as PNG or PDF
    filename = f"triangle_with_trig_{base}_{opposite}.png"
    plt.savefig(filename, bbox_inches='tight', pad_inches=0.1)
    plt.close()

    # Optionally open the image
    img = Image.open(filename)
    img.show()

    print(f"Image saved as {filename}")
if __name__ == "__main__":
    main()
  
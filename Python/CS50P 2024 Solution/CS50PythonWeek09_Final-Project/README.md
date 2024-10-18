# Trigonometric Functions by Ronak Patel

#### Video Demo: https://youtu.be/f6z6uZottb0

#### Description:
This project is a Python-based application designed to calculate and visualize the trigonometric ratios for a right triangle. The application takes the base and opposite sides of the triangle as inputs and then calculates the hypotenuse using the Pythagorean theorem. It subsequently computes the six primary trigonometric ratios: sine, cosine, tangent, secant, cosecant, and cotangent. Additionally, the program generates a visual representation of the triangle along with the calculated trigonometric values.

### Project Structure

The project consists of two primary Python files:

1. **Main Python File (`main.py`)**:
    - This file serves as the core of the application. It handles user input, performs the calculations, and generates the output both in text and graphical form.
    - The key functions in this file include:
        - `BaseOfTriangle()` and `OppositeOfTriangle()`: These functions handle the input of the base and opposite sides of the triangle.
        - `HypotenuseOfTriangle(base, opposite)`: This function calculates the hypotenuse using the formula \( \text{hypotenuse} = \sqrt{\text{base}^2 + \text{opposite}^2} \).
        - `calculation_logic(base, opposite, hypotenuse)`: This function computes the six trigonometric ratios (sin, cos, tan, sec, cosec, cot) using the base, opposite, and hypotenuse.
        - `printer(results)`: This function prints the calculated trigonometric ratios in a readable format.
        - `generate_image(base, opposite, hypotenuse, results)`: This function generates a visual representation of the triangle, annotated with its dimensions and the calculated trigonometric ratios. The generated image is saved as a PNG file and displayed to the user.

    - The program runs in a loop, allowing the user to perform multiple calculations until they choose to terminate the program. It also includes error handling to manage invalid inputs.

2. **Unit Test File (`test_project.py`)**:
    - This file contains unit tests for the core functionalities of the application, ensuring that the calculations performed by the `HypotenuseOfTriangle()` and `calculation_logic()` functions are accurate.
    - The tests are written using the `pytest` framework, which allows for easy validation of the mathematical accuracy of the results.
    - Key tests include:
        - `test_hypotenuse_of_triangle()`: This test verifies that the hypotenuse calculation is accurate for a variety of triangle dimensions.
        - `test_calculation_logic()`: This test ensures that the trigonometric ratios are calculated correctly based on known values.

### Design Choices

Several design decisions were made during the development of this project:

1. **User Input Handling**:
    - The input handling is designed to be straightforward and user-friendly. The program continuously prompts the user for valid inputs and handles incorrect inputs gracefully by providing an error message and reprompting.

2. **Trigonometric Ratio Calculation**:
    - The choice to use functions for each trigonometric ratio ensures clarity and modularity in the code. This modular approach also makes it easier to maintain and expand the project in the future.

3. **Visualization**:
    - The decision to include a graphical representation of the triangle was made to enhance user understanding of the trigonometric concepts. The use of `matplotlib` for visualization and `PIL` for image handling allows for clear and customizable images that display the triangle and its associated trigonometric ratios.

4. **Testing**:
    - Unit tests were implemented to ensure the reliability and correctness of the core calculations. This decision was crucial for validating the mathematical operations and providing confidence in the accuracy of the results.

### How to Run the Project

To run this project, ensure you have Python installed along with the necessary libraries (`matplotlib`, `PIL`, and `pytest`). You can install the required libraries using the following commands:

```bash
pip install matplotlib pillow pytest

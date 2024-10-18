import pytest
import math
from project import HypotenuseOfTriangle, calculation_logic

def test_hypotenuse_of_triangle():
    assert math.isclose(HypotenuseOfTriangle(3, 4), 5.0, rel_tol=1e-9)
    assert math.isclose(HypotenuseOfTriangle(5, 12), 13.0, rel_tol=1e-9)
    assert math.isclose(HypotenuseOfTriangle(8, 15), 17.0, rel_tol=1e-9)

def test_calculation_logic():
    results = calculation_logic(3, 4, 5)
    assert math.isclose(results['sin'], 4/5, rel_tol=1e-9)
    assert math.isclose(results['cos'], 3/5, rel_tol=1e-9)
    assert math.isclose(results['tan'], 4/3, rel_tol=1e-9)
    assert math.isclose(results['sec'], 5/3, rel_tol=1e-9)
    assert math.isclose(results['cosec'], 5/4, rel_tol=1e-9)
    assert math.isclose(results['cot'], 3/4, rel_tol=1e-9)


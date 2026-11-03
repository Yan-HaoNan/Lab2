import importlib.util
from pathlib import Path

import pytest

# Load the sibling file explicitly: this repo is also a submodule named Lab2.
spec = importlib.util.spec_from_file_location("lab2_calculations", Path(__file__).with_name("Lab2.py"))
lab2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lab2)


@pytest.mark.parametrize("values, expected", [([30, 20, 25], (20, 30)), ([-5, -2, -10], (-10, -2)), ([7], (7, 7))])
def test_find_min_max(values, expected):
    assert lab2.find_min_max(values) == expected


@pytest.mark.parametrize("values, expected", [([20, 25, 30], 25), ([-5, 0, 6], 1 / 3), ([2.5], 2.5)])
def test_calc_average(values, expected):
    assert lab2.calc_average(values) == pytest.approx(expected)


@pytest.mark.parametrize("values, expected", [([30, 10, 20], 20), ([40, 10, 30, 20], 25), ([5], 5), ([-3, -1, -2], -2), ([2, 1, 2, 3], 2)])
def test_calc_median_temperature(values, expected):
    original = values.copy()
    assert lab2.calc_median_temperature(values) == expected
    assert values == original


@pytest.mark.parametrize("function", [lab2.find_min_max, lab2.calc_average, lab2.calc_median_temperature])
def test_empty_temperatures(function):
    with pytest.raises(ValueError):
        function([])

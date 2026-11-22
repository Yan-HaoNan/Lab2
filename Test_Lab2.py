import Lab2

def test_calc_average():
    temp=[10.0, 20.0, 30.0]
    result = Lab2.calc_average(temp)
    assert result==20.0

def test_find_min_max():
    temp=[10.0, 20.0,30.0]
    result =Lab2.find_min_max(temp)
    assert result==[10.0, 30.0]

def test_calc_median_temperature():
    temp=[10.0, 20.0,30.0]
    result =Lab2.calc_median_temperature(temp)
    assert result==20.0
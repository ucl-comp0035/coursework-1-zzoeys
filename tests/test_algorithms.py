import algorithms

def test_minimum_returns_correct_value():
    """
    GIVEN the values 2, 4, 8 and 20
    WHEN the values are passed to the minimum function
    THEN the result should equal 2
    """
    values = [2, 4, 8, 20]
    result = algorithms.minimum(values)
    assert result == 2
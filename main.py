def test_square_root():
    assert square_root(4) == 2
    assert square_root(16) == 4
    assert square_root(0) == 0
    try:
        square_root(-1)
    except ValueError as e:
        assert str(e) == "Cannot calculate square root of a negative number"

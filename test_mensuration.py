from mesuring_3d_shapes import square_size,rectangle
import pytest


def test_square_size():
    assert square_size(3)==(12,9)
    assert square_size(7)==(28,49)
    assert square_size(5)==(20,25)
    
def test_rectangle():
        assert rectangle(6,5)==(22,30)
        assert rectangle(7,7)==(28,49)
        assert rectangle(8,5)==(26,40)
        

pytest.main(["-v", "--tb=line", "-rN", __file__])

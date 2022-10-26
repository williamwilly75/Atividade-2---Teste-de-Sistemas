from Menu import Menu
from Coordinate import Coordinate
from Validate_Number import ValidateNumber
import pytest

def test_get_user_coordinateX():
    coordinateX = 10
    assert ValidateNumber.is_number(coordinateX) == True

def test_get_user_coordinateY():
    coordinateY = 20
    assert ValidateNumber.is_number(coordinateY) == True
    
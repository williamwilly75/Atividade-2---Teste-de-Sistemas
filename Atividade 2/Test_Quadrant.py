from Coordinate import Coordinate
from Quadrant import Quadrant
from Validate_Number import ValidateNumber
import pytest

def test_first_quadrant():
    x = 10
    y = 20
    coordinates = Coordinate(x, y)
    quadrant = Quadrant(coordinates)

    result = quadrant.get_quadrant_coordinate()

    assert result == "First"

def test_second_quadrant():
    x = -10
    y = 20
    coordinates = Coordinate(x, y)
    quadrant = Quadrant(coordinates)

    result = quadrant.get_quadrant_coordinate()

    assert result == "Second"

def test_third_quadrant():
    x = -10
    y = -20
    coordinates = Coordinate(x, y)
    quadrant = Quadrant(coordinates)

    result = quadrant.get_quadrant_coordinate()

    assert result == "Third"

def test_fourth_quadrant():
    x = 10
    y = -20
    coordinates = Coordinate(x, y)
    quadrant = Quadrant(coordinates)

    result = quadrant.get_quadrant_coordinate()

    assert result == "Fourth"

def test_null_x_coordinate():
    x = 0
    y = -20
    coordinates = Coordinate(x, y)
    quadrant = Quadrant(coordinates)

    result = quadrant.get_quadrant_coordinate()

    assert result == ""

def test_null_y_coordinate():
    x = 10
    y = 0
    coordinates = Coordinate(x, y)
    quadrant = Quadrant(coordinates)

    result = quadrant.get_quadrant_coordinate()

    assert result == ""

def test_character_coordinateX():
    x = "x"
    
    assert ValidateNumber.is_number(x) == True
    

def test_character_coordinateY():
    y = "y"

    assert ValidateNumber.is_number(y) == True
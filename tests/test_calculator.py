'''My Calculator Test'''
from calculator import operations

def test_addition():
    '''Test that addition function works '''    
    assert operations.add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert operations.subtract(2,2) == 0

def test_divide():
    '''Test that division function works '''    
    assert operations.divide(2,2) == 1

def test_multiply():
    '''Test that multiply function works '''    
    assert operations.multiply(2,2) == 4
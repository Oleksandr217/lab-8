from main_code import add_numbers

def test_addition_positive():
    assert add_numbers(2, 3) == 6  
    
def test_addition_negative():
    assert add_numbers(-1, 1) == 0
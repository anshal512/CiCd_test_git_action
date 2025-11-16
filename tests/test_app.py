from src.app import add_numbers, greet

def test_add_numbers():
    assert add_numbers(2, 3) == 5

def test_greet():
    assert greet("Anshal") == "Hello, Anshal!"

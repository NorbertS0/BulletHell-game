import pytest
from src import KeyInput

# keyMap varaible in KeyInput must be of type dictionary
def test_keyMap_must_be_dict():
    with pytest.raises(TypeError):
        k = KeyInput(1)

# keyMap varaible in KeyInput must have a length of 1 or more
def test_keyMap_must_have_values():
    with pytest.raises(TypeError):
        k = KeyInput(dict())

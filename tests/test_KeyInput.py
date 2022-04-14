import pytest
from src.KeyInput import KeyInput
from pynput.keyboard import Controller

# keyMap varaible in KeyInput must be of type dictionary
def test_keyMap_must_be_dict():
    with pytest.raises(TypeError):
        KeyInput(1)

# keyMap varaible in KeyInput must have a length of 1 or more
def test_keyMap_must_have_values():
    with pytest.raises(ValueError):
        KeyInput(dict())

def test_key_input_empty_when_no_press():
    k = KeyInput({'q':'IsPressed'})
    assert k.detect() == set()

def test_key_input_is_detected():
    k = KeyInput({'q':'IsPressed'})
    keyboard = Controller()
    keyboard.press('q')
    detectedSet = k.detect()
    keyboard.release('q')
    assert detectedSet == set({k.keyMap['q']})

def test_multi_key_input_is_detected():
    k = KeyInput({'q':'IsPressed', 'w':'AnotherKey'})
    keyboard = Controller()
    keyboard.press('q')
    keyboard.press('w')
    detectedSet = k.detect()
    keyboard.release('q')
    keyboard.release('w')
    assert detectedSet == set({k.keyMap['q'],k.keyMap['w']})

def test_remapped_key_input():
    k = KeyInput({'q':'IsPressed'})
    keyboard = Controller()
    k.remap('q', 'w')
    keyboard.press('q')
    detectedSet = k.detect()
    keyboard.release('q')
    assert detectedSet == set()
    keyboard.press('w')
    detectedSet = k.detect()
    keyboard.release('w')
    assert detectedSet == set({k.keyMap['w']})

def test_test_cannot_remap_to_existing_key():
    k = KeyInput({'q':'IsPressed', 'w':'AnotherKey'})
    assert k.remap('q', 'w') == False
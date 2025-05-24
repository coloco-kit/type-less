from ..external import Dog, get_dog, get_dog_with_input, LiteralType
from .. import external
from ..matching import is_equivalent_type
from type_less.inference import guess_return_type
from typing import TypedDict


# Imported


def test_guess_return_type_imported_function():
    assert is_equivalent_type(guess_return_type(get_dog), Dog)

def test_guess_return_type_called_imported_function():
    class TheDogReturns(TypedDict):
        dog: Dog

    def func():
        dog = get_dog()
        return {
            "dog": dog,
        }
    
    assert is_equivalent_type(guess_return_type(func), TheDogReturns)

def test_guess_return_type_imported_function_args():
    class TheDogReturns(TypedDict):
        input: LiteralType
        dog: Dog

    def func():
        dog = get_dog_with_input("test1")
        return dog
    
    assert is_equivalent_type(guess_return_type(func), TheDogReturns)

def test_guess_return_type_imported_module_function_args():
    class TheDogReturns(TypedDict):
        input: LiteralType
        dog: Dog

    def func():
        dog = external.get_dog_with_input("test1")
        return dog
    
    assert is_equivalent_type(guess_return_type(func), TheDogReturns)


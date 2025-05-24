from ..matching import validate_is_equivalent_type
from type_less.inference import guess_return_type
from typing import TypeVar

T = TypeVar("T")
def get_item(item: T) -> T:
    return item

def test_typevar_int():
    def func():
        value = get_item(42)
        return value
    
    assert guess_return_type(func, use_literals=False) == int
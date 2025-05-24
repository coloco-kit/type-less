import pytest
from ..matching import is_equivalent_type
from type_less.inference import guess_return_type
from typing import Awaitable, Literal, TypedDict, Type, TypeVar, Union


MODEL = TypeVar("MODEL", bound="Animal")
class Animal:
    @classmethod
    async def create(cls: Type[MODEL]) -> MODEL:
        return cls()
    
class Cat(Animal):
    color: Literal["black", "orange"]
    has_ears: bool
    
class Collar:
    cat: Awaitable[Cat]


# Async

async def get_cat_async() -> Cat:
    return Cat(color="black", has_ears=True)

@pytest.mark.asyncio
async def test_guess_return_type_follow_function_return_async():
    class TheCatReturns(TypedDict):
        color: Literal["black", "orange"]
        has_ears: bool

    async def func():
        cat = await get_cat_async()
        return {
            "color": cat.color,
            "has_ears": cat.has_ears,
        }
    
    assert is_equivalent_type(guess_return_type(func), TheCatReturns)


# Inherited Async


@pytest.mark.asyncio
async def test_guess_return_type_follow_function_return_async_inherited():
    class TheCatReturns(TypedDict):
        color: Literal["black", "orange"]
        has_ears: bool

    async def func():
        cat = await Cat.create()
        return {
            "color": cat.color,
            "has_ears": cat.has_ears,
        }
    
    assert is_equivalent_type(guess_return_type(func), TheCatReturns)

@pytest.mark.asyncio
async def test_guess_return_type_follow_function_return_async_method():
    class TheCatReturns(TypedDict):
        color: Literal["black", "orange"]
        has_ears: bool

    async def func():
        collar = Collar()
        cat = await collar.cat
        return {
            "color": cat.color,
            "has_ears": cat.has_ears,
        }
    
    assert is_equivalent_type(guess_return_type(func), TheCatReturns)


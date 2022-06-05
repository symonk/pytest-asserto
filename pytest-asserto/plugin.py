import pytest
from asserto import Asserto
import typing


@pytest.fixture
def asserto() -> typing.Type[Asserto]:
    """
    The Asserto class instance for use as a fixture with arguments.
    """
    return Asserto

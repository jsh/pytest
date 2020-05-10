"""A failing test."""

import pytest


@pytest.mark.xfail
def test_failing():
    """A false statement should fail."""
    assert (1, 2, 3) == (3, 2, 1)

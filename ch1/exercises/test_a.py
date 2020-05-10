"""Test other assertions."""

import pytest


def test_inclusion():
    """in tests list inclusion."""
    assert 1 in [1, 2, 3]


def test_inequality():
    """Inequalities should work."""
    assert 2 > 1


@pytest.mark.xfail
def test_not_in():
    """in tests string inclusion."""
    assert "fizz" not in "abcfizzbuzz"

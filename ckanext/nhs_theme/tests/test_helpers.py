"""Tests for helpers.py."""

import ckanext.nhs_theme.helpers as helpers


def test_nhs_theme_hello():
    assert helpers.nhs_theme_hello() == "Hello, nhs_theme!"

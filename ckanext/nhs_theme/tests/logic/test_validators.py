"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.nhs_theme.logic import validators


def test_nhs_theme_reauired_with_valid_value():
    assert validators.nhs_theme_required("value") == "value"


def test_nhs_theme_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.nhs_theme_required(None)

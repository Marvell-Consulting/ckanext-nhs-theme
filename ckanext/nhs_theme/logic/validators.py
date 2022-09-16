import ckan.plugins.toolkit as tk


def nhs_theme_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "nhs_theme_required": nhs_theme_required,
    }

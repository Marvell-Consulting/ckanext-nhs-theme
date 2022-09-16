from flask import Blueprint


nhs_theme = Blueprint(
    "nhs_theme", __name__)


def page():
    return "Hello, nhs_theme!"


nhs_theme.add_url_rule(
    "/nhs_theme/page", view_func=page)


def get_blueprints():
    return [nhs_theme]

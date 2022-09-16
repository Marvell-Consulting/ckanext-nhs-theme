import ckan.plugins.toolkit as tk
import ckanext.nhs_theme.logic.schema as schema


@tk.side_effect_free
def nhs_theme_get_sum(context, data_dict):
    tk.check_access(
        "nhs_theme_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.nhs_theme_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'nhs_theme_get_sum': nhs_theme_get_sum,
    }

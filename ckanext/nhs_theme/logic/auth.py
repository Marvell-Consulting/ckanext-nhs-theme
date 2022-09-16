import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def nhs_theme_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "nhs_theme_get_sum": nhs_theme_get_sum,
    }

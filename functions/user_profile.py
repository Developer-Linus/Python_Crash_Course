def build_profile(first, last, **user_info):
    """
    Build a dictionary of the information we know about user.
    """
    profile = {}
    profile["first_name"] = first.title()
    profile["last_name"] = last.title()

    for key, value in user_info.items():
        profile[key] = value
    return profile


print(build_profile("albert", "einstein", location="princeton", field="physics"))

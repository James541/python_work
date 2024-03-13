def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile('james', 'wagner', location='USA', firstLanguage='JavaScript', secondLanguage='Python')

print(user_profile)
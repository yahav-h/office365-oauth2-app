

class Office365AdminLoginTags:
    EMAIL_FIELD = ("xpath", './/*[contains(@type, "email") or contains(@autocomplete, "username")]')
    NEXT_BUTTON = ("xpath", './/input[contains(@type, "submit") and contains(@value, "Next")]')
    PASSWORD_FIELD = ("xpath", './/input[contains(@type, "password") or contains(@name, "password")]')
    SIGN_IN_BUTTON = ("xpath", './/input[contains(@type, "submit") and contains(@value, "Sign in")]')


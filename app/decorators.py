from functools import wraps
from flask import redirect, url_for
from flask_login import current_user


def role_required(roles):
    if not isinstance(roles, list):
        roles = [roles]
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role not in roles:
                return redirect(url_for('errors.not_authorised'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator
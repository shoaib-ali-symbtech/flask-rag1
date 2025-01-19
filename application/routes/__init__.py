from functools import wraps
from fastapi.requests import Request
from application.utilities.res import APIError
from fastapi import status


def user_login_required(f):
    @wraps(f)
    def decorated_function(request:Request,*args, **kwargs):

        if request.headers.get("authorization") is None:
            return APIError(message="Un-Authorized", status=status.HTTP_401_UNAUTHORIZED).to_json()
        
        return f(request,*args, **kwargs)

    return decorated_function

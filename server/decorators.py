from functools import wraps

def uppercase(func):
    @wraps(func)
    async def do_uppercase(*args, **kwargs):
        resp = await func(*args, **kwargs)
        resp.body = resp.body.decode('utf8').upper().encode()
        return resp
    return do_uppercase

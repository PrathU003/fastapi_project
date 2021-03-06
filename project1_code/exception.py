from fastapi import HTTPException , status

def http_exception():
    return HTTPException(status_code = 404 , detail = 'not found')

 
def successful_response(status_code: int):
    return {
        'status' : status_code , 'transaction' : 'Successful'}

def get_user_exception():    
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = 'Could not validate credentials',
        headers = {'WWW-Authenticate' : 'Bearer'},
    )
    return credentials_exception

def token_exception():
    token_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = 'Incorrect username or password',
        headers = {'WWW-Authenticate' : 'Bearer'},
    )
    return token_exception

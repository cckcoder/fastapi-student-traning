import secrets

from fastapi import Depends, status, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()


async def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    # it like if "johndoe" == "admin99" and "love123" == "#123321#":
    correct_username = secrets.compare_digest(credentials.username, "admin99")
    correct_password = secrets.compare_digest(credentials.password, "#123321#")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

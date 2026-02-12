from jose import JWTError, jwt
from datetime import datetime,timedelta
from . import schema ,database,models
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings


SECRET_KEY=settings.secret_key
ALGORITHM=settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTE=settings.access_token_expire_minutes
 
oauth2_schema=OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data:dict): 
    to_encode=data.copy()

    expire=datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt
def verify_token( token:str,crenditial_expection):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id:str=payload.get("user_id") 
        if not id:
            raise crenditial_expection
        token_data=schema.token_data(id=str(id))
        return token_data
    except JWTError:
        raise crenditial_expection
    
def get_current_user(token:str=Depends(oauth2_schema),db:Session=Depends(database.get_db)):
    credintial_expections=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate crendentials",headers={"WWW.Authenticate":"Bearer"})
    token= verify_token(token,credintial_expections)
    user=db.query(models.User).filter(models.User.id==token.id).first()
    return user 
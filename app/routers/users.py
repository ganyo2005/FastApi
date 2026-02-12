
from .. import  models,schema,util,Oauth2
from fastapi import status,HTTPException,Depends,APIRouter
from .. database import get_db
from sqlalchemy . orm import Session
from .. database import get_db
from typing import List

router=APIRouter(
    prefix="/users",
    tags=["Users"]
)



@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schema.UserRespons)
def crete_user(user:schema.UserLogin,db:Session =Depends(get_db)):
    hashed_password=util.hashed_password(user.password)
    user.password=hashed_password
    new_users= models.User(
        **user.dict())

    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    email=user.email
    return new_users

@router.get("/{id}",response_model=schema.UserRespons)
def get_user(id:int,db:Session =Depends(get_db),current_user:int=Depends(Oauth2.get_current_user)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {id} not found")
    print(current_user.email)
    return user 
@router.get("/",response_model=List[schema.UserRespons])
def get_data(db:Session =Depends(get_db)):
    user=db.query(models.User).all()
    # posts=cursor.execute("""SELECT * from post""")
    # post=cursor.fetchall()us
    return user

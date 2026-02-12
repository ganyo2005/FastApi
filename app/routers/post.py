
from .. import  models,schema,Oauth2
from fastapi import Response,status,HTTPException,Depends,APIRouter
from .. database import SessionLocal,get_db
from sqlalchemy . orm import Session
from .. database import get_db
from sqlalchemy import func
from typing import List,Optional

router=APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

  # print(post)
    # posts=cursor.execute("""SELECT * from post""")
    # post=cursor.fetchall()us


@router.get("/",response_model=List[schema.PostVoteOut])
def get_data(db:Session =Depends(get_db),current_id:int=Depends(Oauth2.get_current_user),Limit:int=10,skip:int=0,search:Optional[str]=""):
    

    post=db.query(models.Post,func.count(models.Votes.post_id).label("Votes")).join(models.Post,models.Votes.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(Limit).offset(skip).all()

    return post

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schema.PostRespons)
def createPost(post:schema.PostCreate,db:Session=Depends(get_db),current_user:int=Depends(Oauth2.get_current_user)):
     
# #    post_dic=new_post.dict()
# #    post_dic["id"]=randrange(0,100)
# #    my_post.routerend(post_dic)
#     cursor.execute("""INSERT INTO post(title,content,published)
#                    VALUES(%s,%s,%s) RETURNING * """,(new_post.title,new_post.content,new_post.published)) 
#     new_post=cursor.fetchone()
#     conn.commit()
    new_post= models.Post(
        user_id=current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
    

@router.get("/{id}",response_model=schema.PostVoteOut) 
def get_post(id:int,db:Session =Depends(get_db)):
    # post=find_post(id)
    # cursor.execute("""SELECT * FROM post WHERE id = %s """,(str(id),))
    # new_post=cursor.fetchone()
    # print(new_post)
    post=db.query(models.Post,func.count(models.Votes.post_id).label("Votes")).join(models.Post,models.Votes.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id==id).first()
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id } was not found")
        # response.status_code=status.HTTP_404_NOT_FOUND

    return post
    
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db:Session =Depends(get_db),currrent_user:int=Depends(Oauth2.get_current_user)):
    # index=get_index(id)
    # cursor.execute("""DELETE FROM post WHERE id = %s RETURNING *""",(str(id),))
    # delete_post=cursor.fetchone()
    # conn.commit()
    post_qurey=db.query(models.Post).filter(models.Post.id==id)
    post=post_qurey.first()

    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id } was not found")
    
    if post.user_id != currrent_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform requested action")


    post_qurey.delete(synchronize_session=False)

    Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}",response_model=schema.PostRespons)
def update_post(id:int,updated_post:schema.PostCreate,db:Session =Depends(get_db),current_user:int=Depends(Oauth2.get_current_user)):
    # cursor.execute(""" UPDATE post SET title=%s, content=%s, published=%s WHERE id=%s RETURNING * """,(post.title,post.content,post.published,str(id,)))
    # conn.commit ()
    # post=cursor.fetchone()
    # print(updated_post)

    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    
    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} was not found")
    
    if post.user_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You are not authorized to perform this qurrey")
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    return post_query.first()
    
from fastapi import FastAPI 
from . import models
from . database import engine
from . routers import post,users,auth,votes
from . config import settings
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)
app=FastAPI() 

origin=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users.router)
app.include_router(post.router)
app.include_router(auth.router)
app.include_router(votes.router)
@app.get("/")
def read_root ():
    return {"Hello": "my name is Nick"}
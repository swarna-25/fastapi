

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import user, post, auth, vote
from .config import settings


#models.Base.metadata.create_all(bind=engine) # do not need this as we are creating tables now via alembic

app = FastAPI()

# origins = ["https://www.google.com","https://www.youtube.com"]
origins = ["*"] #it allows all websites to connect to our api
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=["*"], #allows all http methods 
    allow_headers=["*"],
)


# my_posts=[{"title":"This is title 1","content":"content of post 1","id":1},
#           {"title":"This is title 2", "content":"content of post 2","id":2}]

# def find_post(id):
#     for p in my_posts:
#         if p['id'] ==id:
#             return p
        
# def find_index_post(id):
#     for i,p in enumerate (my_posts):
#         if p['id']==id:
#             return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World pushed to prod via CI/CD pipeline"}

# @app.get("/sqlalchemy")
# def test_posts(db: Session=Depends(get_db)):
#     posts= db.query(models.Post).all()
#     return {"Data": posts}



# @app.post("/posts")
# def create_posts(payLoad: dict = Body(...)): #Body(...) function will extract all json values from postman api request body, will save it as python dictionary and store it in variable payLoad
#     print(payLoad)
#     # return {"message": "successfully created"}
#     return {"new_post": f"title: {payLoad['title']} content: {payLoad['content']}"}

# @app.post("/posts",status_code=status.HTTP_201_CREATED)
# def create_posts(post: schemas.Post): #schema validation from Post class is saved in post variable
    # print(post.title)
    # print(post)
    # print(post.published)
    # print(post.ratings)
    # print(post.model_dump()) #converting pydantic defined values into dictionary
    # return {"data": "new post"}
    # post_dict=post.model_dump()
    # post_dict['id']=randrange(0,10000000)
    # my_posts.append(post_dict)
    # return {"data": post_dict}










    






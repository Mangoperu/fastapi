from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()
my_posts = [{"title" : "title of post 1" , "content" : "content of pst 1" , "id" : "1"},{"title" : "fav food" , "content" : "pizza" , "id" : "2"}];
class Post(BaseModel):
    title : str = "not present"
    content : str = 'not present'
    published : bool = True
    rating : Optional[int] = None


@app.get("/")
async def root():
    return {"message": my_posts}

@app.post("/createpost")
async def createpost(newpost : Post):
    post_dict = newpost.dict();
    post_dict['id'] = str(randrange(0 , 10000000))
    my_posts.append(post_dict)
    return {"its working" : my_posts}


def finding(id):
    for p in my_posts:
        if p["id"] == id:
            return p
    return {"sorry": "post not available"}


@app.get("/posts/latestpost")
def latest_post():
    latestpost = my_posts[len(my_posts)-1]
    return {"detail" : latestpost}


@app.get("/posts/{id}")
def get_post(id : int):
    print(id)
    return {"post detail" : finding(id)}





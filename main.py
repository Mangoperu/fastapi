from fastapi import FastAPI , Response , status
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

@app.post("/createpost" , status_code=status.HTTP_201_CREATED)
async def createpost(newpost : Post):
    post_dict = newpost.dict();
    post_dict['id'] = str(randrange(0 , 10000000))
    my_posts.append(post_dict)
    return {"its working" : my_posts}


def finding(id):
    for p in my_posts:
        if p["id"] == id:
            return p


@app.get("/posts/latestpost")
def latest_post():
    latestpost = my_posts[len(my_posts)-1]
    return {"detail" : latestpost}


@app.get("/posts/{id}")
def get_post(id, response : Response):
    print(id)
    post = finding(id)
    if not post :
        response.status_code = status.HTTP_404_NOT_FOUND
        return {f"post with {id}" : "not found"}
    return {"post detail" : post}





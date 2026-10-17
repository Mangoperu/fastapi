from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
my_posts = {{"title" : "title of post 1" , "content" : "content of pst 1" , "id" : "1"},{"title" : "fav food" , "content" : "pizza" , "id" : "2"}};
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
    print(newpost.rating)
    return {"its working" : "yo"}


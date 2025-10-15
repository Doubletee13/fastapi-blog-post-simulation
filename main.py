from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

class User(BaseModel):
    name: str
    post: str

app = FastAPI() 

all_post = {}
post_id = 0


    

@app.get("/users/{id}")
def get_post(id:int):
    if not id or id not in all_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found")
    details = all_post[id]
    return {"message":"post retrieved successfully",
            "content":details
            }


@app.post("/users",status_code=status.HTTP_201_CREATED)
def add_post(user: User):
    global post_id
    post_id += 1
    name = user.name
    post = user.post
    all_post.update({post_id:{"Name":name,"Post":post}})
    return {
        "message":"post created successfully",
        "content":user
    }

@app.patch("/users/{id}")
def update_post(id:int,user: User):
    if not id or id not in all_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found")
    post = user.post
    all_post[id]["Post"]=post
    return {
        "message":"post updated successfully",
        "changes":post
    }


@app.delete("/users/{id:int}")
def delete_post(id):
    if not id or id not in all_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found")
    all_post.pop(id)
    return {
        "message":"post deleted successfully"
    }

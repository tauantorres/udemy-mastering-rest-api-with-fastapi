from typing import List
from pydantic import BaseModel

class UserPostIn(BaseModel):
    body: str

class UserPost(UserPostIn):
    id: int

class CommentIn(BaseModel):
    body: str
    post_id: int

class Comment(CommentIn):
    id: int

class UserPostWithComments(BaseModel):
    post: UserPost
    comments: List[Comment] 
        

# {
#     "post": {"id": 0, "body": "The post"},
#     "comments": [
#         {
#             "id": 0, 
#             "post_id": 0,
#             "body": "The first comment", 
#         },
#         {
#             "id": 1, 
#             "post_id": 0,
#             "body": "The second comment", 
#         }
#     ]
# }

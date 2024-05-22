from typing import List
from pydantic import BaseModel, ConfigDict

class UserPostIn(BaseModel):
    body: str

class UserPost(UserPostIn):
    id: int
    model_config = ConfigDict(from_attributes=True)

class CommentIn(BaseModel):
    body: str
    post_id: int

class Comment(CommentIn):
    id: int
    model_config = ConfigDict(from_attributes=True)

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

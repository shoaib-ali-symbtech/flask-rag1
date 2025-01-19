
import uvicorn
from application import create_app
app = create_app()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
    
    


# from typing import Union
# from fastapi import FastAPI, HTTPException
# from dotenv import load_dotenv
# import boto3
# load_dotenv()


# # Initialize Cognito client
# cognito_client = boto3.client('cognito-idp', region_name=COGNITO_REGION)

# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World updated" }


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.get("/list-users/")
# def list_users():
#     USER_POOL_ID = "your_user_pool_id"
#     try:
#         response = cognito_client.list_users(UserPoolId=USER_POOL_ID)
#         return {"users": response["Users"]}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

    
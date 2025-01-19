import os
from fastapi import APIRouter
from fastapi import Request
from application.routes import user_login_required
from application.utilities.res import APIResponse
app_auth = APIRouter()




@app_auth.get("/")
@user_login_required
def get_loggedin_detail(request:Request):
  return {"USer":"Login"}
  


  
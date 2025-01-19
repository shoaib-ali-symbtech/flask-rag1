from dotenv import load_dotenv
load_dotenv()
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
 
 
def create_app():
 
    app = FastAPI()
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
        
    # user route
    from application.routes.auth import app_auth
 
    app.include_router(app_auth, prefix="/user",tags=["User auth"])

 

 
  
 
    return app
 
 
 

 
 
 
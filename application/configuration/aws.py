import os
class AWSConfig:
    AWS_ACCESS_KEY_ID:str = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY:str = os.environ.get("AWS_SECRET_ACCESS_KEY")
    COGNITO_REGION:str = os.environ.get("COGNITO_REGION")
    COGNITO_USER_POOL_ID:str = os.environ.get("COGNITO_USER_POOL_ID")
  
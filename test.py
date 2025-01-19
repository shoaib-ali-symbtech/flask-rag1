from dotenv import load_dotenv
import boto3
import os
load_dotenv()


print(os.environ["COGNITO_REGION"])

cognito_client = boto3.client('cognito-idp', region_name=os.environ["COGNITO_REGION"])
response = cognito_client.list_users(UserPoolId="ap-south-1_5lY3leXXZ")
print(response["Users"])
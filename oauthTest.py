from requests_oauthlib import OAuth2Session
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("client_id")
client_secrets = os.getenv("client_secrets")
redirect_uri = "http://localhost:5000/"
scope = ["email","profile"]

oauth = OAuth2Session(client_id,redirect_uri=redirect_uri,scope=scope)
authorization_url,state = oauth.authorization_url(
    
)
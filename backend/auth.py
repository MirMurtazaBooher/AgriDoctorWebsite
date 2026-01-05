import os
from fastapi import Header, HTTPException



def verify_api_key(x_api_key: str = Header(...)):
    MASTER_API_KEY = os.getenv("MASTER_API_KEY")
    if x_api_key != MASTER_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

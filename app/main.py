from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 
from fastapi.middleware.trustedhost import TrustedHostMiddleware 
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session 
from db import engine, Base, get_db 
from routers import auth, file 
from config import settings 
import logging 





if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
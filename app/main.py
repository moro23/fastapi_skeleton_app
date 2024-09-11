from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 
from fastapi.middleware.trustedhost import TrustedHostMiddleware 
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session 
from db import engine, Base, get_db 
from routers import auth, file 
from config import settings 
import logging 

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI instance
app = FastAPI(title="FastAPI Web Application with SQLAlchemy ORM")

# Add CORS middleware (optional: adjust settings as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add Trusted Host Middleware (optional)
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"],  # Adjust this for production
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(file.router, prefix="/file", tags=["file"])

# Static files (optional, for serving static assets)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Dependency for getting the database session
@app.middleware("http")
async def db_session_middleware(request, call_next):
    response = None
    async with get_db() as db:
        response = await call_next(request)
    return response

# Startup event to create database tables
@app.on_event("startup")
async def on_startup():
    logger.info("Starting up the application...")
    # Create all tables
    Base.metadata.create_all(bind=engine)

# Shutdown event
@app.on_event("shutdown")
async def on_shutdown():
    logger.info("Shutting down the application...")

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}



if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
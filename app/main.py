from fastapi import FastAPI,Request,status, HTTPException
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.trustedhost import TrustedHostMiddleware 
import logging 


from db.init_models import create_tables



from apis.routers import router as api_router


# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Adding our api routes 
def include(app):
    app.include_router(api_router)


def initial_data_insert():
   
    db = SessionLocal()
    try:
        init_db(db)
        create_super_admin(db)
    finally:
        db.close()

def start_application():
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
    include(app)
    create_tables()
    # initial_data_insert()
    return app

app = start_application() 



# # Include routers
# app.include_router(auth.router, prefix="/auth", tags=["auth"])
# app.include_router(file.router, prefix="/file", tags=["file"])

# # Static files (optional, for serving static assets)
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Dependency for getting the database session
# @app.middleware("http")
async def db_session_middleware(request, call_next):
    response = None
    async with get_db() as db:
        response = await call_next(request)
    return response

# Startup event to create database tables
@app.on_event("startup")
async def on_startup():
    logger.info("Starting up the application...")
  

# Shutdown event
@app.on_event("shutdown")
async def on_shutdown():
    logger.info("Shutting down the application...")

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
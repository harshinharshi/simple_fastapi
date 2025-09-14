from fastapi import FastAPI

# Import the database components
from app.db.session import engine
from app.db.session import Base
# We need to import the model so that SQLAlchemy knows about it
from app.models import item

# Import the API router
from app.api.v1.endpoints import items

# This line creates the database tables if they don't exist
# It uses the engine and looks for all classes that inherit from Base
Base.metadata.create_all(bind=engine)

# Create the FastAPI app instance
app = FastAPI(title="My Todo API")


@app.get("/")
def read_root():
    """
    A simple root endpoint to confirm the API is running.
    """
    return {"status": "ok", "message": "Welcome to the Todo API!"}


# Include the items router in our main app
app.include_router(items.router, prefix="/api/v1/items", tags=["items"])